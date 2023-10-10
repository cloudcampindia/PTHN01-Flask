from flask import Flask, request
from flask_migrate import Migrate

from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.__init__(app)

from models.project import Project

migrate = Migrate(app, db)

from flask_restful import Api
from resources.project import ProjectListResource, ProjectResource
api = Api(app)

api.add_resource(ProjectListResource, '/')
api.add_resource(ProjectResource, '/projects/<int:project_id>')


if __name__ == '__main__':
    app.run(debug=True)


"""
flask db init
flask db migrate -m "Add Project table"
flask db upgrade
flask db upgrade
"""