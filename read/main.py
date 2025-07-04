from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
#prueba 2.0 workflow SSM Aent
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, apellido, cedula, celular, email FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    users = [
        {"id": row[0], "name": row[1], "apellido": row[2], "cedula": row[3], "celular": row[4], "email": row[5]}
        for row in rows
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
