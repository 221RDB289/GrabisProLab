import pandas as pd
import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'istroman21.mysql.eu.pythonanywhere-services.com',
    'user': 'istroman21',
    'password': '-',
    'database': 'istroman21$basketDB'
}

file_paths = [
    "/home/istroman21/basketball/fullGames23.csv",
    "/home/istroman21/basketball/fullGames24.csv",
    "/home/istroman21/basketball/fullGames25.csv"
]
def determine_year(file_path):
    if "23" in file_path:
        return 2022
    elif "24" in file_path:
        return 2023
    elif "25" in file_path:
        return 2024
    else:
        raise ValueError(f"Unknown year for file: {file_path}")

def insert_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    year = determine_year(file_path)

    insert_query = """
    INSERT INTO Games (Visitor_neutral, Vpts, Home_neutral, Hpts, Year)
    VALUES (%s, %s, %s, %s, %s);
    """
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        for _, row in df.iterrows():
            cursor.execute(insert_query, (
                row['Visitor/Neutral'],
                row['VPTS'],
                row['Home/Neutral'],
                row['HPTS'],
                year
            ))

        # Commit the transaction
        connection.commit()
        print(f"Data from {file_path} inserted successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Insert data from all CSV files
for file_path in file_paths:
    insert_data_from_csv(file_path)

