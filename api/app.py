from enum import unique
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
import bcrypt
import requests

app = Flask(__name__)
CORS(app)
                           

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY = os.environ.get("SECRET_KEY")
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__ (self, username, password):
        self.username = username
        self.password = password

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    
    if user:
        if bcrypt.checkpw(bytes(password, 'utf-8'), user.password):
            login_user(user)
            return jsonify({"success": "user access granted"})
        else:
            return jsonify({"error": {"password" :"Passwords do not match"}})
    else:
        return jsonify({"error": {"username":"This username does not exist"}})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"})
        
    else:
        hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'),bcrypt.gensalt())
        user = User(username, hashed_password)

        db.session.add(user)
        db.session.commit()
        return jsonify({"success": "User registered"})


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()

@app.route('/categories')
def categories():
    key = os.getenv('NYT_KEY')
    response = requests.get(f"https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={key}")
    print('key', key)
    return jsonify({"data": response.json()})