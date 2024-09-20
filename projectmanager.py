from project import Project

class Projectmanager:
    def __init__(self) -> None:
        self.projects = []

    def add_project(self, name, start_date, end_date, budget):
        new_project = Project(name, start_date, end_date, budget)
        self.projects.append(new_project)
        print(f"Project '{name}' added successfully!")

    def view_projects(self):
        if not self.projects:
            print('No Projects Available')
            return
        
        print('Current Projects')

        for i, project in enumerate(self.projects, start = 1):
            print(f'{i}.{project}')

    # Method for removing project

    def remove_project(self, index):
        if 0 <= index < len(self.projects):
            removed_project = self.projects.pop(index)
            print(f'Project {removed_project.name} removed successfully')
        else:
            print('Invalid Project Index')