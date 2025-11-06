# Auther: Joseph Kracht
# Last Modified: 11/6/2025
# Title: Employee Class

# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, id, department, title):
        self.name = name
        self.id = id
        self.department = department
        self.title = title

    def display_data(self):
        print("Name:", self.name)
        print("ID Number:", self.id)
        print("Department:", self.department)
        print("Job Title:", self.title)


# Create a list for the employees
all_employees = []

# Create employee1 and add it him to the list
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
all_employees.append(employee1)

# Create employee2 and add it him to the list
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
all_employees.append(employee2)

# Create employee3 and add it him to the list
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
all_employees.append(employee3)

# Loop though each employ and print its data
for employee in all_employees:
    employee.display_data()
    print()
