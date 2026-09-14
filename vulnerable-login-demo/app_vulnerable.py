from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Login (Vulnerable Version)</h2>
        <form action="/login" method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # VULNERABLE: raw string formatting into SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()

    if result:
        return "Login successful!"
    return "Login failed."

if __name__ == '__main__':
    app.run(debug=True)
