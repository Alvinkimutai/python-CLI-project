from sqlalchemy import create_engine
from project import Base
from projectmanager import ProjectManager
from task import Task
import datetime
from colorama import Fore, Style

def main():
    DATABASE_URL = 'sqlite:///projects.db'
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Create tables here Base.metadata.create_all(engine)

    prj_manager = ProjectManager(engine)

    while True:
        print(f"\n{Fore.CYAN}=== Construction Management System ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Add Project{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. View Projects{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Remove Project{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Add Task{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Update Task Progress{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6. View Tasks{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}7. Remove Task{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}8. Manage Labor{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}9. Manage Materials{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}10. Manage Equipment{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}11. Exit{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}======================================={Style.RESET_ALL}")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            name = input("Enter project name: ")
            start_date = datetime.datetime.strptime(input("Enter Start Date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(input("Enter End Date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            budget = float(input("Enter Budget: "))
            prj_manager.add_project(name, start_date, end_date, budget)

        elif choice == "2":
            prj_manager.view_projects()

        elif choice == "3":
            prj_manager.view_projects()
            index = int(input("Enter project index to remove: "))
            prj_manager.remove_project(index)

        elif choice == "4":
            prj_manager.view_projects()
            index = int(input("Enter project index to add task: "))
            task_name = input("Enter task name: ")
            prj_manager.add_task(index, task_name)

        elif choice == "5":
            prj_manager.view_projects()
            project_index = int(input("Enter project index to view tasks: "))
            tasks = prj_manager.session.query(Task).filter(Task.project_id == project_index + 1).all()
            if tasks:
                for i, task in enumerate(tasks):
                    print(f"{i}. {task}")
                task_index = int(input("Enter task index to update progress: "))
                progress = float(input("Enter new progress (0-100): "))
                prj_manager.update_task_progress(task_index, progress)
            else:
                print("No tasks found for this project.")

        elif choice == "6":
            prj_manager.view_projects()
            project_index = int(input("Enter project index to view tasks: "))
            tasks = prj_manager.session.query(Task).filter(Task.project_id == project_index + 1).all()
            if tasks:
                for i, task in enumerate(tasks):
                    print(f"{i}. {task}")
            else:
                print("No tasks found for this project.")

        elif choice == "7":
            prj_manager.view_projects()
            project_index = int(input("Enter project index to remove task from: "))
            tasks = prj_manager.session.query(Task).filter(Task.project_id == project_index + 1).all()
            if tasks:
                for i, task in enumerate(tasks):
                    print(f"{i}. {task}")
                task_index = int(input("Enter task index to remove: "))
                prj_manager.remove_task(task_index, project_index)
            else:
                print("No tasks found for this project.")

        elif choice == "8":
            print(f"{Fore.YELLOW}--- Labor Management ---{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}1. Add Labor{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}2. View Labor{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}3. Remove Labor{Style.RESET_ALL}")
            labor_choice = input("Choose an option (1-3): ")

            if labor_choice == "1":
                name = input("Enter labor name: ")
                hourly_rate = float(input("Enter hourly rate: "))
                prj_manager.add_labor(name, hourly_rate)
            elif labor_choice == "2":
                prj_manager.view_labor()
            elif labor_choice == "3":
                prj_manager.view_labor()
                index = int(input("Enter labor index to remove: "))
                prj_manager.remove_labor(index)

        elif choice == "9":
            print(f"{Fore.YELLOW}--- Material Management ---{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}1. Add Material{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}2. View Materials{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}3. Remove Material{Style.RESET_ALL}")
            material_choice = input("Choose an option (1-3): ")

            if material_choice == "1":
                name = input("Enter material name: ")
                unit_cost = float(input("Enter unit cost: "))
                quantity = int(input("Enter quantity: "))
                prj_manager.add_material(name, unit_cost, quantity)
            elif material_choice == "2":
                prj_manager.view_materials()
            elif material_choice == "3":
                prj_manager.view_materials()
                index = int(input("Enter material index to remove: "))
                prj_manager.remove_material(index)

        elif choice == "10":
            print(f"{Fore.YELLOW}--- Equipment Management ---{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}1. Add Equipment{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}2. View Equipment{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}3. Remove Equipment{Style.RESET_ALL}")
            equipment_choice = input("Choose an option (1-3): ")

            if equipment_choice == "1":
                name = input("Enter equipment name: ")
                rental_cost_per_day = float(input("Enter rental cost per day: "))
                prj_manager.add_equipment(name, rental_cost_per_day)
            elif equipment_choice == "2":
                prj_manager.view_equipment()
            elif equipment_choice == "3":
                prj_manager.view_equipment()
                index = int(input("Enter equipment index to remove: "))
                prj_manager.remove_equipment(index)

        elif choice == "11":
            print(f"{Fore.RED}Exiting the System. Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
