from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from views.routes import *
from views.police_home import *

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')