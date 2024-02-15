"""
As and an English instructor I manually make class plans for each of my students monthly
and calculate their monthly fee. This programm will read through a students file and use the 
information provided to plan classes for each student or group. It should generate an invoice for 
each student requested.

Author: Sampson Ngobi 
Date:  2019-03-15
"""

"""
Programm should be able to 

1. Add a student to a dictionary that has student information 
2. Remove a student when neccessary 
3. Update a students information 
4. Compute number of classes per month
5. Generate Invoices for individual students, groups or all student
6. Print out invioce  with total amount due and save it as a text file 

"""

# Create a dictionary to store student information
students = []

# Add a student to a list of dictionaries that stores student information
def add_student(students):
    name = input("Enter Student's Name : ")
    id = int(input("Enter Student's ID : "))
    no_of_classes = int(input("Enter number of classes per week: "))
    cost_per_class = float(input("Enter Cost Per Class: $"))

    if any(student['id'] == id for student in students):
        print('Student already exists')
        return False

    new_student = {'name': name, 'id': id, 'classes_per_week': no_of_classes, 'cost_per_class': cost_per_class}
    students.append(new_student)
    print(students)

add_student(students)



