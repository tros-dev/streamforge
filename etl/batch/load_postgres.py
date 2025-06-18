import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv("POSTGRES_URL"))
cursor = conn.cursor()

def load_data():
    with open('data/processed/clean_data.csv') as f:
        next(f)  # Skip header
        cursor.copy_from(f, 'raw_table', sep=',')
    conn.commit()

if __name__ == '__main__':
    load_data()
