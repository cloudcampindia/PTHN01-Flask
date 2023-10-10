from extensions import db

# Project Table ORM model
class Project(db.Model):
    __tablename__ = "project"

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    main_category = db.Column(db.String(100), nullable=False)
    goal = db.Column(db.Float, nullable=False)

    def data(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'category': self.category,
            'main_category': self.main_category,
            'goal': self.goal
        }

    @classmethod
    def get_by_project_id(cls, project_id):
        return cls.query.filter_by(project_id=project_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()