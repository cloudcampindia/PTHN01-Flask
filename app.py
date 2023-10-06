from flask import Flask, request
from flask_restful import Api
from resources.project import ProjectListResource, ProjectResource


# print(__name__) # __main__
app = Flask(__name__)
api = Api(app)

api.add_resource(ProjectListResource, '/')
api.add_resource(ProjectResource, '/projects/<int:project_id>')


"""
In Memory database. This list gets back to its original state. What ever we add to this will be deleted once the server is restarted
"""

if __name__ == '__main__':
    app.run(debug=True)