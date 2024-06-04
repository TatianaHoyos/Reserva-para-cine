from flask import Flask
from app import app
from app.controllers.reservation_controller import *

if __name__ == '__main__':
    app.run()
