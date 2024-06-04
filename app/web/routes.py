from flask import Blueprint
from app.controllers.reservation_controller import create_reservation_controller

web = Blueprint('web', __name__)

@web.route('/reservations', methods=['POST'])
def create_reservation():
    return create_reservation_controller()
