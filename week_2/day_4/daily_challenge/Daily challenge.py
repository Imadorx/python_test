import requests
import random
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="countries_db",
        user="postgres",          
        password="20020429", 
        host="localhost",
        port="5432"
    )

def fetch_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_country(country):
    conn = get_connection()
    cur = conn.cursor()

    name = country.get("name", {}).get("common", "Unknown")
    capital = country.get("capital", ["Unknown"])[0] if country.get("capital") else "Unknown"
    flag = country.get("flag")
    subregion = country.get("subregion", "Unknown")
    population = country.get("population", 0)

    cur.execute("""
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, capital, flag, subregion, population))

    conn.commit()
    cur.close()
    conn.close()


def main():
    countries = fetch_countries()
    selected = random.sample(countries, 10)  

    for country in selected:
        save_country(country)
        print(f"Saved {country['name']['common']}")

if __name__ == "__main__":
    main()
