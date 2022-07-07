from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from celery_app import CeleryFactory

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
celery = CeleryFactory()
