import os
import psycopg2
from flask import Flask, make_response, render_template, request

# Obtener opciones desde las variables de entorno, con valores por defecto
option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")

app = Flask(__name__)

# Conectar a la base de datos
def connect_db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="database.default.svc.cluster.local",
        port="5432"
    )
    return conn

# Crear tabla si no existe
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS votes (id SERIAL PRIMARY KEY, vote VARCHAR(255) NOT NULL)")
    conn.commit()
    cursor.close()
    conn.close()

create_table()

@app.route("/", methods=['POST', 'GET'])
def hello():
    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        process_vote(vote)

    resp = make_response(render_template(
        'index.html',
        option_a=option_a,
        option_b=option_b,
        vote=vote,
    ))
    return resp

def process_vote(vote):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO votes (vote) VALUES (%s)", (vote,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Vote processed successfully")
    except Exception as e:
        print("Error processing vote:", e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
