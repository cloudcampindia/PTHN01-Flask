projects_list = []

def get_project_id():
    """
    Return the Project ID information based on the list of projects
    present in our in-memory database
    """
    if projects_list:
        return projects_list[-1].data['project_id'] + 1
    return 1

"""
"name": "The Songs of Adelaide & Abullah",
"category": "Poetry",
"main_category": "Publishing",
"goal": 1000.0
"""

class Project:
    """
    Template to be used when creating a project in
    our database
    """
    def __init__(self, name, category, main_category, goal):
        self.project_id = get_project_id()
        self.name = name
        self.category = category
        self.main_category = main_category
        self.goal = goal
    
    @property
    def data(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'category': self.category,
            'main_category': self.main_category,
            'goal': self.goal
        }