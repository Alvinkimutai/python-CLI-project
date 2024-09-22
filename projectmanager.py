
from project import Project, Session

class ProjectManager:
    def __init__(self) -> None:
        self.session = Session()

    def add_project(self, name, start_date, end_date, budget):
        new_project = Project(name=name, start_date=start_date, end_date=end_date, budget=budget)
        self.session.add(new_project)
        self.session.commit()
        print(f"Project '{name}' added successfully!")

    def view_projects(self):
        projects = self.session.query(Project).all()
        if not projects:
            print('No Projects Available')
            return
        
        print('Current Projects:')
        for i, project in enumerate(projects, start=1):
            print(f'{i}. {project}')

    def remove_project(self, index):
        project_to_remove = self.session.query(Project).get(index + 1)  # Index is zero-based
        if project_to_remove:
            self.session.delete(project_to_remove)
            self.session.commit()
            print(f'Project {project_to_remove.name} removed successfully')
        else:
            print('Invalid Project Index')


