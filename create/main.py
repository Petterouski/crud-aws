from flask import Flask, request, jsonify
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

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (name, apellido, cedula, celular, email)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (data["name"], data["apellido"], data["cedula"], data["celular"], data["email"]))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": user_id}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
