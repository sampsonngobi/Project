# imort neccessary  libraries - CSV and tkinter
import csv
import tkinter as tk
from tkinter import messagebox


#create a heading list
heading = ['ID', 'NAME', 'NUMBER OF CLASSES', "COST PER CLASS"]

#create an empty list to store student infomation
student_info = []

#this function adds student to the  student info list
def add_student(student_info):

    #create a second window to collect students info
    add_window = tk.Toplevel()
    add_window.title("Add Student")
    add_window.geometry('600x400')
    add_window.configure(bg = '#333333')

    #add a frame
    add_frame = tk.Frame(add_window, bg= "#333333", height=150, width=700)
    add_frame.pack(pady=20, padx=50)


    #Create variables for each field in the form
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    classes_var = tk.StringVar()
    cost_var = tk.StringVar()

    #this function is called when the add button is  clicked
    def add_to_database():
        #get input values
        id_value = int(id_var.get())
        name_value = name_var.get()
        num_classes = int(classes_var.get())
        cost = float(cost_var.get())

        #check if student exits 
        if any(student[0] == id_value for student in student_info):
            messagebox.showwarning("Warning","Student ID already exists. Choose a new ID")
        
        else:
            #creat new student and append new student information to the database
            new_student = [id_value, name_value, num_classes, cost]
            student_info.append(new_student)

            #call the write student function
            write_to_file("student-info.csv", student_info, heading= None)

            messagebox.showinfo("Success!","New student added successfully.")

            #close the add window
            add_window.destroy()

    id_label = tk.Label(add_frame, text="Student ID:")
    id_label.grid(row=0, column=0, pady=15)
    id_entry = tk.Entry(add_frame, textvariable=id_var)
    id_entry.grid(row=0, column=1, pady=15)

    name_label = tk.Label(add_frame, text="Name:")
    name_label.grid(row=1, column=0, pady=15)
    name_entry = tk.Entry(add_frame, textvariable=name_var)
    name_entry.grid(row=1, column=1, pady=15)

    class_label = tk.Label(add_frame, text="Number of Classes:")
    class_label.grid(row=2, column=0, pady=15)
    class_entry = tk.Entry(add_frame, textvariable=classes_var)
    class_entry.grid(row=2, column=1, pady=15)

    cost_label = tk.Label(add_frame, text="Cost per Class: $")
    cost_label.grid(row=3, column=0, pady=15)
    cost_entry = tk.Entry(add_frame, textvariable=cost_var)
    cost_entry.grid(row=3, column=1, pady=15)

    add_student_button = tk.Button(add_frame, text='Add Student', command=lambda : add_to_database())
    add_student_button.grid(row=4, column=1, pady=15)



            

#this function writes the new student to a csv file
def write_to_file(filename, student_info, heading= None):

    #open a file
    with open("student-info.csv", "wt", newline="") as student_file:
        
        #create a writer object
        writer = csv.writer(student_file)

        #write the heading row first (if there is one)
        if heading is not None:
            writer.writerow(heading)
            
        for  student in student_info:
            writer.writerow(student)




    







#create a window
window =tk.Tk()
window.title("Student Manger")
window.geometry('600x400')
window.configure(bg = '#333333')

#add a frame on the window for responsiveness
frame = tk.Frame(window, bg= "#333333", height=150, width=700)
frame.pack(pady=20, padx=50)

#Add and remove buttons link to functions 
add_button_student = tk.Button(frame , text="Add Student", width=30, command=lambda: [add_student(student_info)])
add_button_student.grid(row=1, column=1, pady= 40)

remove_button_student = tk.Button(frame , text="Remove Student", width=30)
remove_button_student.grid(row=2, column=1, pady= 40)



window.mainloop()