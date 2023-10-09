from flask import Flask, request
from flask_restful import Api
from resources.project import ProjectListResource, ProjectResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProjectListResource, '/')
api.add_resource(ProjectResource, '/projects/<int:project_id>')


if __name__ == '__main__':
    app.run(debug=True)