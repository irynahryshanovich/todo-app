import os
import certifi

from flask import Flask
from main.routes import main
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGOURI"), tlsCAFile=certifi.where())
    app.db = client.get_default_database()
    app.register_blueprint(main)

    return app
