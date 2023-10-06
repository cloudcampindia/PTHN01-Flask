from flask import Flask, request
from http import HTTPStatus

# print(__name__) # __main__
app = Flask(__name__)

"""
In Memory database. This list gets back to its original state. What ever we add to this will be deleted once the server is restarted
"""
"""
{
    "name": "The Songs of Adelaide & Abullah",
    "category": "Poetry",
    "main_category": "Publishing",
    "goal": 1000.0
},
{
    "name": "Greeting From Earth: ZGAC Arts Capsule For ET",
    "category": "Narrative Film",
    "main_category": "Film & Video",
    "goal": 30000.0
},
{
    "category": "Narrative Film",
    "goal": 45000.0,
    "main_category": "Film & Video",
    "name": "Where is Hank?"
}
"""
projects = []

def get_project_id(projects):
    """
    Return the Project ID information based on the list of projects
    present in our in-memory database
    """
    if projects:
        return projects[-1]['project_id'] + 1
    return 1

# http://127.0.0.1:5000/ GET
@app.route("/", methods=["GET"])
def list_projects():
    """
    Returns the list of projects
    """
    return projects, HTTPStatus.OK

# http://127.0.0.1:5000/add POST
@app.route("/add", methods=["POST"])
def add_project():
    """
    Adds a new project to the list of projects
    """
    data = request.get_json()
    data['project_id'] = get_project_id(projects)
    projects.append(data)
    return {}, HTTPStatus.CREATED


@app.route("/project/<int:project_id>", methods=["GET"])
def get_project_by_id(project_id):
    """
    Fetch a project by its ID
    """
    for project in projects:
        if project["project_id"] == project_id:
            return project, HTTPStatus.OK
    else:
        return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND


"""
{
    "category": "Narrative Film",
    "goal": 45000.0,
    "main_category": "Film & Video",
    "name": "Where is Hank?"
}
"""

@app.route("/project/<int:project_id>", methods=["PUT"])
def update_project_by_id(project_id):
    """
    Update a project by its ID
    """
    data = request.get_json()
    for project in projects:
        if project["project_id"] == project_id:
            project["name"] = data["name"]
            project["category"] = data["category"]
            project["goal"] = data["goal"]
            project["main_category"] = data["main_category"]
            return project, HTTPStatus.OK
    else:
        return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND

@app.route("/project/<int:project_id>", methods=["DELETE"])
def delete_project_by_id(project_id):
    """
    Delete a project by its ID
    """
    for project in projects:
        if project["project_id"] == project_id:
            projects.remove(project)
            return '', HTTPStatus.NO_CONTENT
    else:
        return {'message': f"Project with ID: {project_id} is not found"}, HTTPStatus.NOT_FOUND

if __name__ == '__main__':
    app.run(debug=True)