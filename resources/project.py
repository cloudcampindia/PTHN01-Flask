from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.project import Project

class ProjectListResource(Resource):

    def get(self):
        """
        Returns the list of projects
        """
        projects_list = Project.query.all()
        data = []
        for project in projects_list:
            data.append(project.data())
        return {'data': data}, HTTPStatus.OK


    def post(self):
        """
        Adds a new project to the list of projects
        """
        data = request.get_json()
        project = Project(name=data["name"], 
                          category=data["category"], 
                          main_category=data["main_category"], 
                          goal=data["goal"])
        project.save()
        return {}, HTTPStatus.CREATED

class ProjectResource(Resource):


    def get(self, project_id):
        """
        Fetch a project by its ID
        """
        project = Project.get_by_project_id(project_id=project_id)
        if project is None:
            return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND
        return {'data': project.data()}, HTTPStatus.OK


    def put(self, project_id):
        """
        Update a project by its ID
        """
        data = request.get_json()
        project = Project.get_by_project_id(project_id=project_id)
        if project is None:
            return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND
        
        project.name = data["name"]
        project.category = data["category"]
        project.goal = data["goal"]
        project.main_category = data["main_category"]

        project.save()

        return project.data(), HTTPStatus.OK

    def delete(self, project_id):
        """
        Delete a project by its ID
        """
        project = Project.get_by_project_id(project_id=project_id)
        if project is None:
            return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND
        
        project.delete()
        return {}, HTTPStatus.NO_CONTENT