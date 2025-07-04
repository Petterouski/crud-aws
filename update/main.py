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

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users
        SET name = %s, apellido = %s, cedula = %s, celular = %s, email = %s
        WHERE id = %s
    """, (data["name"], data["apellido"], data["cedula"], data["celular"], data["email"], user_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "User updated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
