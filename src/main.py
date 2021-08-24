from flask import Flask
from flask_cors import CORS
from flask import request,jsonify
import os
import sys
sys.path.append(os.getcwd())
from src.simulator import simulate_reply

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')

    def check_server():
        return "Server running"

    @app.route('/index', methods = ["POST"])
    def index():
        post_url = request.headers.get('post_url')
        
        response = simulate_reply(post_url)

        return jsonify(response)

    return app
