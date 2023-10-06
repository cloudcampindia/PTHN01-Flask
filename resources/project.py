from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.project import projects_list, Project

class ProjectListResource(Resource):

    def get(self):
        """
        Returns the list of projects
        """
        data = []
        for project in projects_list:
            data.append(project.data)
        return data, HTTPStatus.OK


    def post(self):
        """
        Adds a new project to the list of projects
        """
        data = request.get_json()
        project = Project(name=data["name"], 
                          category=data["category"], 
                          main_category=data["main_category"], 
                          goal=data["goal"])
        projects_list.append(project)
        return {}, HTTPStatus.CREATED

class ProjectResource(Resource):


    def get(self, project_id):
        """
        Fetch a project by its ID
        """
        for project in projects_list:
            if project.project_id == project_id:
                return project.data
        else:
            return {'message': f"Project with ID: {project_id} is not found"}


    def put(self, project_id):
        """
        Update a project by its ID
        """
        data = request.get_json()
        for project in projects_list:
            if project.project_id == project_id:
                project.name = data["name"]
                project.category = data["category"]
                project.goal = data["goal"]
                project.main_category = data["main_category"]
                return project.data
        else:
            return {'message': f"Project with ID: {project_id} is not found"}

    def delete(self, project_id):
        """
        Delete a project by its ID
        """
        for project in projects_list:
            if project.project_id == project_id:
                projects_list.remove(project)
                return ''
        else:
            return {'message': f"Project with ID: {project_id} is not found"}