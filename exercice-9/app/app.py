import os
import time

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
        database=os.environ.get("DB_NAME", "postgres"),
    )

def ensure_db_ready(max_attempts=30, delay_seconds=1):
    last_error = None

    for _ in range(max_attempts):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        CREATE TABLE IF NOT EXISTS visites (
                            id SERIAL PRIMARY KEY,
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                        """
                    )
            return
        except Exception as error:
            last_error = error
            time.sleep(delay_seconds)

    raise last_error


def ensure_visites_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS visites (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

@app.route("/")
def home():
    ensure_visites_table()
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM visites")
            count = cur.fetchone()[0]
    return f"<h1>Visites: {count}</h1>"

@app.route("/visites", methods=["POST"])
def add_visite():
    ensure_visites_table()
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO visites DEFAULT VALUES")
            conn.commit()
            cur.execute("SELECT COUNT(*) FROM visites")
            count = cur.fetchone()[0]
    return jsonify({"total": count}), 200

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    ensure_db_ready()
    app.run(host="0.0.0.0", port=5000)