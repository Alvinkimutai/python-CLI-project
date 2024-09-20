class Project:

    def __init__(self, name, start_date, end_date, budget) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        

    # Defining method to return info
    def __str__(self) -> str:
        return f'Project Name: {self.name}, Start Date: {self.start_date}, End Date: {self.end_date}, Budget: {self.budget}'
    

   