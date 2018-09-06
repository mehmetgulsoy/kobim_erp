from flask import Blueprint

bp = Blueprint('malzeme', __name__, template_folder='sablon')

from app.malzeme import rota  # noqa
