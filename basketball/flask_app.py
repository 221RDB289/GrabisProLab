from flask import Flask, render_template, redirect, url_for, request, flash, session
from config import Config
from db import db, bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User, Games
from BB_NEW_V2 import predictP

# Flask aplikācijas inicializācija un konfigurācija
app = Flask(__name__, template_folder='template')
app.config.from_object(Config)

# Inicializē datubāzi un bcrypt (paroles šifrēšanai)
db.init_app(app)
bcrypt.init_app(app)

# Izveido datubāzes tabulas, ja tās vēl neeksistē
with app.app_context():
    db.create_all()

# Flask-Login konfigurācija
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Norāda, kurā lapā lietotāju novirzīt, ja nav pieteicies

# Funkcija, lai ielādētu lietotāju pēc ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Funkcija, kas atgriež visas unikālās komandu nosaukumus no datubāzes
def get_teams():
    query = """
    SELECT DISTINCT team_name FROM (
        SELECT Visitor_Neutral AS team_name FROM Games
        UNION
        SELECT Home_Neutral AS team_name FROM Games
    ) AS unique_teams;
    """
    result = db.session.execute(query)
    return [row.team_name for row in result]

# Mājas lapa - ja lietotājs nav pieslēdzies, novirza uz login lapu
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return redirect(url_for("predict"))

# Lietotāja izlogošana un sesijas notīrīšana
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# Lietotāja reģistrācijas funkcija
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        email = request.form["email"]
        favorite_team = request.form.get("favorite_team")
        age = request.form.get("age")

        # Pārbauda, vai lietotājvārds vai e-pasts jau eksistē
        if User.query.filter_by(username=username).first():
            flash("Lietotājvārds jau eksistē. Izvēlaties citu.", "danger")
        elif User.query.filter_by(email=email).first():
            flash("E-pasts jau tiek izmantots.", "danger")
        else:
            # Izveido jaunu lietotāju un saglabā datubāzē
            user = User(
                username=username,
                password=password,
                email=email,
                favorite_team=favorite_team,
                age=int(age) if age else None
            )
            db.session.add(user)
            db.session.commit()
            flash("Konts izveidots! Lūdzu pieslēdzaties.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

# Lietotāja pieslēgšanās funkcija
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):

            # Saglabā lietotāja informāciju sesijā
            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = user.is_admin

            # Novirza uz atbilstošo lapu (administratora vai prognozes lapa)
            return redirect(url_for("admin" if user.is_admin else "predict"))
        else:
            flash("Nepareizs lietotājvārds vai parole", "danger")
    return render_template("login.html")

# Funkcija, lai apskatītu visus spēļu datus (ar lapošanas funkcionalitāti)
@app.route("/all_games")
def all_games():
    if "user_id" not in session:
        flash("Lūdzu pieslēdzaties sākumā.", "danger")
        return redirect(url_for("login"))

    ROWS_PER_PAGE = 10  # Spēļu skaits vienā lapā
    page = request.args.get('page', 1, type=int)

    result = db.session.execute("SELECT * FROM Games")
    games = [dict(row) for row in result]

    # Kopējais spēļu skaits un lapu skaits
    total_games = len(games)
    total_pages = (total_games // ROWS_PER_PAGE) + (1 if total_games % ROWS_PER_PAGE else 0)

    # Izvēlētās lapas spēļu saraksts
    start_index = (page - 1) * ROWS_PER_PAGE
    games_page = games[start_index:start_index + ROWS_PER_PAGE]

    return render_template("all_games.html", games=games_page, page=page, total_pages=total_pages)

# Komandu statistikas lapa (ar lapošanu)
@app.route("/team_stats")
def team_stats():
    if "user_id" not in session:
        flash("Lūdzu pieslēdzaties sākumā.", "danger")
        return redirect(url_for("login"))

    ROWS_PER_PAGE = 10
    page = request.args.get('page', 1, type=int)

    result = db.session.execute("SELECT * FROM team_performance")
    games = [dict(row) for row in result]

    total_games = len(games)
    total_pages = (total_games // ROWS_PER_PAGE) + (1 if total_games % ROWS_PER_PAGE else 0)
    start_index = (page - 1) * ROWS_PER_PAGE
    games_page = games[start_index:start_index + ROWS_PER_PAGE]

    return render_template("team_stats.html", games=games_page, page=page, total_pages=total_pages)

# Spēļu prognozēšanas lapa
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user_id" not in session:
        flash("Lūdzu pieslēdzaties sākumā.", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":
        team1 = request.form.get("team1")
        team2 = request.form.get("team2")

        # Pārbauda, vai komandas ir izvēlētas un vai tās nav vienādas
        if not team1 or not team2 or team1 == team2:
            flash("Lūdzu izvēlaties divas dažādas komandas.", "danger")
            return redirect(url_for("predict"))

        # Izsauc prognozēšanas funkciju un nosaka uzvarētāju
        prediction = predictP(team1, team2)
        winner = team1 if prediction[0][0] > prediction[0][1] else team2
        score = f"{round(prediction[0][0])} - {round(prediction[0][1])}"

        return render_template(
            "predict.html",
            teams=get_teams(),
            winner=winner,
            score=score,
            selected_team1=team1,
            selected_team2=team2
        )

    return render_template("predict.html", teams=get_teams())

# Aplikācijas palaišana
if __name__ == "__main__":
    app.run(debug=True)
