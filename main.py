from projectmanager import ProjectManager
import datetime
from colorama import Fore, Style

def main():
    prj_manager = ProjectManager()

    while True:
        print(f"\n{Fore.CYAN}=== Construction Management System ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Add Project{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. View Projects{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Remove Project{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Exit{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}======================================={Style.RESET_ALL}")

        choice = input("Enter your choice (1-4): ")

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
            print(f"{Fore.RED}Exiting the System. Goodbye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()


