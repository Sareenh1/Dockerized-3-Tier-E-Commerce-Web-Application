from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'myappuser',
    'password': 'password',
    'host': 'db-instance-private-ip',
    'database': 'myappdb'
}

@app.route('/')
def index():
    return "Hello from Flask!"

@app.route('/data', methods=['GET'])
def get_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table")
    result = cursor.fetchall()
    connection.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
