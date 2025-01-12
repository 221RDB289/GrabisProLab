import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.losses import MeanSquaredError

def process_year_data(game_file, standings_file):
    pd_data = pd.read_csv(game_file)
    inputs_raw = pd_data.drop(columns=['Date', 'Start (ET)', 'VPTS', 'HPTS', 'Box', 'HZ', 'Attend', 'LOG', 'Arena', 'Notes']).to_numpy()
    inputs = np.array([[hash(each[0]) % 10000, hash(each[1]) % 10000] for each in inputs_raw], dtype=float)
    targets = pd_data.drop(columns=['Date', 'Start (ET)', 'Visitor/Neutral', 'Home/Neutral', 'Box', 'HZ', 'Attend', 'LOG', 'Arena', 'Notes']).to_numpy()

    s_data = pd.read_csv(standings_file)
    s_raw = s_data.drop(columns=['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']).to_numpy()

    inputs_s = []
    for each_i in inputs:
        each_i_kopa = [each_i[0], each_i[1]]
        for each_s in s_raw:
            if each_i[0] == hash(each_s[1]) % 10000:
                each_i_kopa.append(each_s.tolist()[0])
                for each in each_s.tolist()[2:]:
                    each_i_kopa.append(eval(each))
            elif each_i[1] == hash(each_s[1]) % 10000:
                each_i_kopa.append(each_s.tolist()[0])
                for each in each_s.tolist()[2:]:
                    each_i_kopa.append(eval(each))
        inputs_s.append(each_i_kopa)
    return np.array(inputs_s), targets

def model_preparation():
    inputs_s23, targets_23 = process_year_data('fullGames23.csv', 'standings23.csv')
    inputs_s24, targets_24 = process_year_data('fullGames24.csv', 'standings24.csv')
    inputs_s25, targets_25 = process_year_data('fullGames25.csv', 'standings25.csv')

    all_inputs = np.concatenate([inputs_s23, inputs_s24, inputs_s25])
    all_targets = np.concatenate([targets_23, targets_24, targets_25])

    model = tf.keras.Sequential([
        tf.keras.Input((34,)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(68, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(102, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(68, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(34, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dense(2)
    ])

    model.compile(optimizer='adam', loss=MeanSquaredError(), metrics=['accuracy'])
    model.summary()

    model.fit(all_inputs, all_targets, epochs=10, verbose=0)

    model.evaluate(all_inputs, all_targets, verbose=1)
    model.save("BBV69.keras")

def load_model():
    loaded_model = tf.keras.models.load_model('BBV69.keras')
    return loaded_model

def test_model():
    model = load_model()

    inputs_s23, targets_23 = process_year_data('fullGames23.csv', 'standings23.csv')
    inputs_s24, targets_24 = process_year_data('fullGames24.csv', 'standings24.csv')

    all_inputs = np.concatenate([inputs_s23, inputs_s24])
    all_targets = np.concatenate([targets_23, targets_24])


    loss, mae = model.evaluate(all_inputs, all_targets, verbose=1)
    avg_target = np.mean(all_targets)
    accuracy_percentage = 100 - (mae / avg_target * 100)

    print(f"Testēšanas zaudējums (Loss): {loss}")
    print(f"Testēšanas vidējais absolūtais kļūda (MAE): {mae}")
    print(f"Testēšanas precizitāte: {accuracy_percentage}%")

def predictP(komanda1, komanda2):
    s_data = pd.read_csv('standings25.csv')
    s_raw = s_data.drop(columns=['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']).to_numpy()
    predictojamais = [hash(komanda1)%1000, hash(komanda2)%1000]
    for each in s_raw:
        if each[1] == komanda1:
            predictojamais.append(each[0])
            for each2 in each.tolist()[2:]:
                predictojamais.append(eval(each2))
    for each in s_raw:
        if each[1] == komanda2:
            predictojamais.append(each[0])
            for each2 in each.tolist()[2:]:
                predictojamais.append(eval(each2))

    model = load_model()
    print(np.array(predictojamais).reshape(1, -1))
    prediction = model.predict(np.array(predictojamais).reshape(1, -1))
    print(prediction)
    return prediction

if __name__ == "__main__":
    # model_preparation()
    # test_model()
    predictP("Milwaukee Bucks","Utah Jazz")