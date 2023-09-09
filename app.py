from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

conn_str = 'DRIVER={SQL Server};SERVER=bootcampserver2.database.windows.net;DATABASE=bootcampsep4server2;UID=bootcamp;PWD=Pass@123'

conn = pyodbc.connect(conn_str)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 30 * FROM SalesLT.Customer')
    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    return render_template('index.html', data=data, columns=column_names)

if __name__ == "__main__":
    app.run(debug=True)

