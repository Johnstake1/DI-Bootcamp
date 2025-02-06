import requests
import random
import psycopg2
from psycopg2 import sql

def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200: #if code is 200, the request was successfull
        return response.json()
    else:
        raise Exception("Failed to get countries")

def get_random_countries(countries, count=10):
    return random.sample(countries, count)

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS countries (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                capital VARCHAR(255),
                flag TEXT,
                subregion VARCHAR(255),
                population BIGINT
            )
            """
        )
        conn.commit()

def insert_countries(conn, countries):
    with conn.cursor() as cur:
        for country in countries:
            name = country.get("name", {}).get("common", "Unknown")
            capital = country.get("capital", ["Unknown"])[0]
            flag = country.get("flags", {}).get("png", "")
            subregion = country.get("subregion", "Unknown")
            population = country.get("population", 0)

            cur.execute(
                """
                INSERT INTO countries (name, capital, flag, subregion, population)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (name, capital, flag, subregion, population)
            )
        conn.commit()

def main():
    # Database connection parameters. Change these to your own values. The DB must be created in Postgress beforehand
    db_params = {
        "dbname": "REST_API_COUNTRIES",
        "user": "postgres",
        "password": "6760",
        "host": "localhost",
        "port": "5432"
    }
    
    # Fetch and process data
    countries = get_countries()
    random_countries = get_random_countries(countries)
    
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    create_table(conn)
    insert_countries(conn, random_countries)
    
    conn.close()
    print("10 random countries inserted successfully.")

if __name__ == "__main__":
    main()
