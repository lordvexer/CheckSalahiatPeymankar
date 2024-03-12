from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Connect to SQL Server database
server = 'SHAFAFTVEDC-SRV'
database = 'info'
username = 'py'
password = 'Aa@1234@'
driver = '{ODBC Driver 17 for SQL Server}'  # Adjust the driver name if needed

conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +';PORT=1433;DATABASE=' + database +';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search', methods=['POST'])
def search():
    userID = request.form['userID']

    # Query the SQL Server database for details related to the input user ID
    cursor.execute("SELECT * FROM InfoUsers WHERE UserID=?", (userID,))
    user = cursor.fetchone()

    return render_template('details.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
