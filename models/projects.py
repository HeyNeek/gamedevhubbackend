from db import db

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=True)
    dev = db.relationship("DevModel", back_populates="projects")