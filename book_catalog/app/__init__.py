#app/init.py

import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def create_app(config_type):     # dev , test or prod

    app = Flask(__name__)
    #app = Flask(__name__)
    configuration = os.path.join(os.getcwd(),'config',config_type+'.py')

    # 'C:\\Users\\NEX4VGV\\PycharmProjects\\book_catalog\\config\\dev.py'


    app.config.from_pyfile(configuration)

    db.init_app(app)


    from app.catalog import main  # import blueprint

    app.register_blueprint(main)

    return app