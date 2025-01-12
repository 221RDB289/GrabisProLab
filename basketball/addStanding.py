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
    "/home/istroman21/basketball/standings23.csv",
    "/home/istroman21/basketball/standings24.csv",
    "/home/istroman21/basketball/standings25.csv"
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

    # Ensure the columns in the CSV match the table
    insert_query = """
    INSERT INTO team_performance (
        Rk, Team, Overall, Home, Road, Conference_E, Conference_W,
        Division_A, Division_C, Division_SE, Division_NW, Division_P, Division_SW,
        All_Star_Pre, All_Star_Post, Margin_3, Margin_10, Year
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Check that the dataframe contains the expected columns
        expected_columns = [
            'Rk','Team', 'Overall', 'Home', 'Road', 'Conference E', 'Conference W',
            'Division A', 'Division C', 'Division SE', 'Division NW', 'Division P', 'Division SW',
            'All-Star Pre', 'All-Star Post', 'Margin 3', 'Margin 10'
        ]

        # If any columns are missing, raise an error
        missing_columns = set(expected_columns) - set(df.columns)
        if missing_columns:
            raise ValueError(f"Missing columns in CSV: {', '.join(missing_columns)}")

        for _, row in df.iterrows():
            cursor.execute(insert_query, (
                row['Rk'],
                row['Team'],
                row['Overall'],
                row['Home'],
                row['Road'],
                row['Conference E'],
                row['Conference W'],
                row['Division A'],
                row['Division C'],
                row['Division SE'],
                row['Division NW'],
                row['Division P'],
                row['Division SW'],
                row['All-Star Pre'],
                row['All-Star Post'],
                row['Margin 3'],
                row['Margin 10'],
                year
            ))

        # Commit the transaction
        connection.commit()
        print(f"Data from {file_path} inserted successfully.")

    except Error as e:
        print(f"Database Error: {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Insert data from all CSV files
for file_path in file_paths:
    insert_data_from_csv(file_path)
