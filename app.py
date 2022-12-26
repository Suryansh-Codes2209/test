from flask import Flask,render_template , redirect, url_for, request , Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('Login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('registration.html')

    
if __name__ == "__main__":
    app.run(debug=True)