from app import app
from models import db,Project

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # creating projects
        project1 = Project(
            name='Project Tracker',
            description='The Project-Tracker Application is a React-based web application designed to manage and display data related to cohorts, projects, and project members. It utilizes Redux for state management and React Table for efficient data display and manipulation. The application provides features for creating, editing, deleting, and viewing details of different entities, ensuring an intuitive user experience for administrators.',
            github_url = 'https://github.com/aggreyrc/Project-Tracker-frontend',
            project_link = "https://project-tracker-frontend-wpnn.vercel.app/"
        )
        
        project2 = Project(
            name='Tools Management System',
            description='This is a Store Management System for a company that is used to check the stocks at any given time. This system is used at an engineering store, to minimize the current tools theft that was observed by the store department employees.',
            github_url = 'https://github.com/monalisasabina/PH-4-PROJECT-TOOLS-MANAGEMENT',
            project_link = "https://store-management-system-7tfm.onrender.com/"
        )
        
        # Adding projects to session
        db.session.add(project1)
        db.session.add(project2)
        db.session.commit()
        
        print ('Data seeded successfully')
        
if __name__== "__main__":
    seed_data()
    