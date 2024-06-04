from flask import Flask
from app.config import Config

app = Flask(__name__, template_folder='web/templates')
app.config.from_object(Config)

# Importar controladores y configurar rutas aquí
