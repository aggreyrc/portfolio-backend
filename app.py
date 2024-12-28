import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db,Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Home
class Home(Resource):
    def get(self):
        return {
               "message": " 🗂️ Welcome to tmy portfolio API 🗂️",
               "api-version": "vi",
               "description": "Portfolio",
               "available_endpoints": [
                   "/projects"
               ]
          },200
api.add_resource(Home, '/')

# Projects
class Projects(Resource):
    # Fetching all projects
    def get(self):
        try:
            project_list = []
            projects = Project.query.all()
            for project in projects:
                project_dict = {
                    "id": project.id,
                    "name": project.name,
                    "description": project.description,
                    "github_url": project.github_url,
                    "project_link": project.project_link
                }
                project_list.append(project_dict)
            return make_response(project_list, 200)
        except Exception as e:
            # Log the error (optional)
            print(f"Error fetching projects: {e}")
            # Return an error response
            return make_response({"error": "An error occurred while fetching projects."}, 500)

api.add_resource(Projects, '/projects')



if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)
