from flask import Flask
from application.models import db
# , User, Role
from application.resources import api
from config import DevelopmentConfig
from flask_security import SQLAlchemyUserDatastore, Security
from application.sec import datastore 

def create_app():
        app = Flask(__name__)
        app.config.from_object(DevelopmentConfig)
        db.init_app(app)
        api.init_app(app)
        # datastore = SQLAlchemyUserDatastore(db, User, Role)
        app.security = Security(app, datastore)
        with app.app_context():
                import application.views
        return app

app= create_app()

if __name__=='__main__':
        app.run(debug=True)