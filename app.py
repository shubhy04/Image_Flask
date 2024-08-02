import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from flask_cors import CORS
from dbconfig import connect, connectDynamicDB
from mysql.connector import Error

# Load environment variables from .env filepip 
load_dotenv()

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "*"}})

# Example route to demonstrate accessing environment variables
@app.route('/', methods=["GET"])
def index(): # Default value can be specified
    try:
        conn = connect()
        if conn is not None:
            Qry = "select * from users;";
            cursor = conn.cursor(dictionary=True)
            cursor.execute(Qry)
            users = cursor.fetchall()
            return jsonify({"users": users}, {"Success": True})
        else:
            return jsonify({"Error": {"Message": "Please Verify DB Settings"}}, {"Success": False})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}}, {"Success": False})
    finally:
        if conn is not None:
            cursor.close()
            conn.close()

@app.route('/home', methods=["GET"])
def home(): # Default value can be specified
    try:
        conn = connectDynamicDB()
        if conn is not None:
            Qry = "select * from users;";
            cursor = conn.cursor(dictionary=True)
            cursor.execute(Qry)
            users = cursor.fetchall()
            return jsonify({"users": users}, {"Success": True})
        else:
            return jsonify({"Error": {"Message": "Please Verify DB Settings"}}, {"Success": False})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}}, {"Success": False})
    finally:
        if conn is not None:
            cursor.close()
            conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        conn = connect()
        if conn is not None:
            error = None
            if request.method == 'POST':
                # Get form data
                email = request.form['email']
                password = request.form['pswd']

                cursor = conn.cursor(dictionary=True)

                # Execute the SQL query to find the user
                cursor.execute(
                    'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
                user = cursor.fetchone()

                # Close the cursor
                cursor.close()
                conn.close()
                if user:
                    # Store user information in session
                    session['loggedin'] = True
                    session['id'] = user['user_id']
                    session['name'] = user['name']

                    # Redirect to dashboard
                    return redirect(url_for('dashboard'))
                else:
                    error = 'Invalid username or password'

            return render_template('login.html', error=error)
        else:
            return 'Error: Could not connect to the database', 500
    except Error as e:
        print(e)
        return 'Error: Login Failed', 500

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        conn = connect()
        if conn is not None:
            if request.method == 'POST':
                # Get form data
                name = request.form['name']
                email = request.form['email']
                password = request.form['pswd']
                phone = request.form['phone']
                address = request.form['address']
                gender = request.form['gender']

                cursor = conn.cursor()

                # Execute the SQL query to insert data into the database
                cursor.execute('INSERT INTO users (name, email, password, phone, address, gender) VALUES (%s, %s, %s, %s, %s, %s)', 
                    (name, email, password, phone, address, gender))
                conn.commit()
                cursor.close()
                conn.close()

                # Redirect to login page after registration
                return redirect(url_for('login'))

            return render_template('register.html')
        else:
            return 'Error: Could not connect to database', 500
    except Error as e:
        print(e)
        return 'Error: Registration failed', 500


if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"))
