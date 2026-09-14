from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Login (Patched Version)</h2>
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
    # SAFE: parameterized query — input is treated as data, not code
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        return "Login successful!"
    return "Login failed."

if __name__ == '__main__':
    app.run(debug=True)
