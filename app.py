import sqlite3
from flask import Flask, request
app = Flask(__name__)
@app.route("/search")
def search():
    name = request.args.get("name")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name='" + name + "'"
    result = conn.execute(query)
    return str(result.fetchall())
app.run()
