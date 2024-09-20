from projectmanager import Projectmanager


def main():

    prj = Projectmanager()

    while True:
        print('\n Construction Management System')

        print('1. Add Project')
        print('2. View Project')
        print('3. Remove Project')
        print('4. Exit')

        choice = input("Enter your choice : ")


        # Responding according to user choice

        if choice == "1":

            name = input("Enter project name:")

            start_date = input("Enter Start Date: (YYYY-MM-DD):")

            end_date = input('Enter End Date: (YYYY/MM/DD):')

            budget =  float(input('Enter Budget:'))

            prj.add_project(name, start_date, end_date, budget)

        elif choice == '2':
            prj.view_projects()
        
        elif choice == '3':
            prj.view_projects()
            index = int(input('Enter project index to remove:'))
            prj.remove_project(index)

        elif choice == '4':
            print('Exiting the System')
            break
        else :
            print("Invalid choice. Please Try Again ")

if __name__ == '__main__':
    main()
