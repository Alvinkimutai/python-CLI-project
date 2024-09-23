from sqlalchemy.orm import sessionmaker
from project import Project
from task import Task
from labor import Labor
from material import Material
from equipment import Equipment

class ProjectManager:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def add_project(self, name, start_date, end_date, budget):
        new_project = Project(name=name, start_date=start_date, end_date=end_date, budget=budget)
        self.session.add(new_project)
        self.session.commit()
        print(f"Project '{name}' added successfully.")

    def view_projects(self):
        projects = self.session.query(Project).all()
        if projects:
            for i, project in enumerate(projects):
                print(f"{i}. {project}")
        else:
            print("No projects found.")

    def remove_project(self, index):
        projects = self.session.query(Project).all()
        if 0 <= index < len(projects):
            project_to_remove = projects[index]
            self.session.delete(project_to_remove)
            self.session.commit()
            print(f"Project '{project_to_remove.name}' removed successfully.")
        else:
            print("Invalid project index.")

    def add_task(self, project_index, task_name):
        projects = self.session.query(Project).all()
        if 0 <= project_index < len(projects):
            project = projects[project_index]
            new_task = Task(name=task_name, project_id=project.id)
            self.session.add(new_task)
            self.session.commit()
            print(f"Task '{task_name}' added to project '{project.name}' successfully.")
        else:
            print("Invalid project index.")

    def update_task_progress(self, task_index, progress):
        task = self.session.query(Task).get(task_index + 1)
        if task:
            task.progress = progress
            self.session.commit()
            print(f"Updated progress for task '{task.name}' to {progress}%.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index, project_index):
        tasks = self.session.query(Task).filter(Task.project_id == project_index + 1).all()
        if 0 <= task_index < len(tasks):
            task_to_remove = tasks[task_index]
            self.session.delete(task_to_remove)
            self.session.commit()
            print(f"Task '{task_to_remove.name}' removed successfully.")
        else:
            print("Invalid task index.")

     # Labor Management
    def add_labor(self, name, hourly_rate):
        new_labor = Labor(name=name, hourly_rate=hourly_rate)
        self.session.add(new_labor)
        self.session.commit()
        print(f"Labor '{name}' added successfully.")

    def view_labor(self):
        labor_list = self.session.query(Labor).all()
        if labor_list:
            for labor in labor_list:
                print(labor)
        else:
            print("No labor found.")

    def remove_labor(self, labor_index):
        labor_list = self.session.query(Labor).all()
        if 0 <= labor_index < len(labor_list):
            labor_to_remove = labor_list[labor_index]
            self.session.delete(labor_to_remove)
            self.session.commit()
            print(f"Labor '{labor_to_remove.name}' removed successfully.")
        else:
            print("Invalid labor index.")

    # Material Management
    def add_material(self, name, unit_cost, quantity):
        new_material = Material(name=name, unit_cost=unit_cost, quantity=quantity)
        self.session.add(new_material)
        self.session.commit()
        print(f"Material '{name}' added successfully.")

    def view_materials(self):
        materials = self.session.query(Material).all()
        if materials:
            for material in materials:
                print(material)
        else:
            print("No materials found.")

    def remove_material(self, material_index):
        materials = self.session.query(Material).all()
        if 0 <= material_index < len(materials):
            material_to_remove = materials[material_index]
            self.session.delete(material_to_remove)
            self.session.commit()
            print(f"Material '{material_to_remove.name}' removed successfully.")
        else:
            print("Invalid material index.")

    # Equipment Management
    def add_equipment(self, name, rental_cost_per_day):
        new_equipment = Equipment(name=name, rental_cost_per_day=rental_cost_per_day)
        self.session.add(new_equipment)
        self.session.commit()
        print(f"Equipment '{name}' added successfully.")

    def view_equipment(self):
        equipment_list = self.session.query(Equipment).all()
        if equipment_list:
            for equipment in equipment_list:
                print(equipment)
        else:
            print("No equipment found.")

    def remove_equipment(self, equipment_index):
        equipment_list = self.session.query(Equipment).all()
        if 0 <= equipment_index < len(equipment_list):
            equipment_to_remove = equipment_list[equipment_index]
            self.session.delete(equipment_to_remove)
            self.session.commit()
            print(f"Equipment '{equipment_to_remove.name}' removed successfully.")
        else:
            print("Invalid equipment index.")
