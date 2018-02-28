##
## __init__.py
##

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# after pip install flask-bootstrap, import module
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# set variable to call Bootstrap module
bootstrap = Bootstrap(app)

from app import routes, models


