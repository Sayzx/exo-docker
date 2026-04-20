from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    count = r.incr("visites")
    return f"<h1>Visiteur n°{count}</h1>"

@app.route("/reset")
def reset():
    r.set("visites", 0)
    return "Compteur remis à zéro", 200