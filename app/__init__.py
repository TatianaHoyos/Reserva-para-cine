from flask import Flask
from app.config import Config
import os


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
app.config.from_object(Config)
app.secret_key = os.urandom(24)