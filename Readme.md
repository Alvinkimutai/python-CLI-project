# EASY Construction Manager #
- EASY Construction Manger is a CLI in python that allows stakeholders in the construction business manage their projects. It is suitable for any field of construction i.e. **Road/Highway construction**, **Buildings** and Even **water projects**.

### link to a video describing the project ##
[https://drive.google.com/file/d/10_pno-ydDMaOtNFaOTEtVE9PKzaodu10/view?usp=sharing]

***
## Composition ##
- Easy is composed of seven python files, a database file, pycache files and Pipfile for the dependencies: 
1. **main.py** - Imports data and this is where CLI is implemented
2. **project.py** - Creates the project table in the database
3. **projectmanager.py** - contains all methods that add functionality to various classes
4. **equipment.py** - Creates equipment table in the database
5. **labor.py** - Creates labor table in the database
6. **materials.py** - Creates the materials table in the database
7. **task.py** - Creates a table for Tasks in a particular project 
8. **projects.db** - Stores all the relational data created in table form 
9. **pycache files** - files created due to imports

***
## Setting up and running the code ##

- Fork and clone the repository into your local machine
- Open the Repository in Visual Studio Code
- Install **SQLite Viewer** extension to be able to view the tables in the database
- Enter the virtual environment **pipenv shell**
- Run **pipenv install** to install all the dependencies
- Install **SQLalchemy** using **pipenv install sqlalchemy** in the terminal ***ensure to be in the virtual env***
- Install **colorama** using **pip install colorama** - used to style the CLI
- Run the file **main.py** to open the CLI in the terminal and select the 
