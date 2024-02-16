import csv
import tkinter as tk
from tkinter import messagebox

# Create a heading list
heading = ['ID', 'NAME', 'NUMBER OF CLASSES', "COST PER CLASS"]

# Create an empty list to store student information
student_info = []



# Function to add a student to the student info list and write to file
def add_student():
    # Create a second window to collect student info
    add_window = tk.Toplevel()
    add_window.title("Add Student")
    add_window.geometry('600x400')
    add_window.configure(bg='#333333')

    # Add a frame
    add_frame = tk.Frame(add_window, bg="#333333", height=150, width=700)
    add_frame.pack(pady=20, padx=50)

    # Create variables for each field in the form
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    classes_var = tk.StringVar()
    cost_var = tk.StringVar()

    # This function is called when the add button is clicked
    def add_to_database():
        # Get input values
        id_value = int(id_var.get())
        name_value = name_var.get()
        num_classes = int(classes_var.get())
        cost = float(cost_var.get())

        # Check if student exists
        if any(student[0] == str(id_value) for student in load_student_data("student-ifo.csv")):
            messagebox.showwarning("Warning", "Student ID already exists. Choose a new ID")
        else:
            # Create a new student and append new student information to the database
            new_student = [id_value, name_value, num_classes, cost]
            student_info.append(new_student)

            # Call the write student function
            write_to_file("student-info.csv", student_info, heading)

            messagebox.showinfo("Success!", "New student added successfully.")

            # Close the add window
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

    add_student_button = tk.Button(add_frame, text='Add Student', command=add_to_database)
    add_student_button.grid(row=4, column=1, pady=15)


def load_student_data(filename):

    students = []

    try:
        with open("student-info.csv", "rt") as student_file:

            reader = csv.reader(student_file)

            # Skip the heading row
            next(reader, None)

            #add  each row to the student list 
            for row in reader:
                students.append(row)

    except FileNotFoundError:
        messagebox.showwarning("Warning", f"File '{student_file}' not found.")
    except  Exception as e:
         messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    return students
        


# Function to write student information to a CSV file
def write_to_file(filename, student_info, heading=None):

    # Open a file for writing 
    with open(filename, "wt", newline="") as student_file:
        # Create a writer object
        writer = csv.writer(student_file)
        # Write the heading row first (if there is one)
        if heading is not None:
            writer.writerow(heading)
        for student in student_info:
            writer.writerow(student)

def remove_student():

    remove_window = tk.Toplevel()
    remove_window.title("Remove Student")
    remove_window.geometry('600x400')
    remove_window.configure(bg='#333333')

    # Add a frame
    remove_frame = tk.Frame(remove_window, bg="#333333", height=150, width=700)
    remove_frame.pack(pady=20, padx=50)

    # Create variables for the id entry
    id_var = tk.StringVar()

    # This function is called when the remove student button is clicked
    def remove_from_database():
        global student_info  # Assuming student_info is a global variable

        id_value = id_var.get()

        confirmation = False

    # Check if the student with the specified ID exists
        if any(student[0] == str(id_value) for student in load_student_data("student-info.csv")):

        # Confirm that you want to delete
            confirmation = messagebox.askyesno("Confirm Removal", "Are you sure you want to delete this student")

        if confirmation:
            # Remove the student with the specified ID
            student_info = [student for student in student_info if student[0] != str(id_value)]

            # Call the write student function to update the file
            write_to_file("student-info.csv", student_info, heading)

            messagebox.showinfo("Success!", f"Student with ID {id_value} removed successfully.")
        else:
            messagebox.showwarning("Warning", f"Student with ID {id_value} not found.")
    # Close the remove window
        remove_window.destroy()

        


            # Get the index of the student to remove from the list and then remove it

    id_label = tk.Label(remove_frame, text="Student ID:")
    id_label.grid(row=0, column=0, pady=15)
    id_entry = tk.Entry(remove_frame, textvariable=id_var)
    id_entry.grid(row=0, column=1, pady=15)


    remove_student_button = tk.Button(remove_frame, text="Remove Student", command=remove_from_database)
    remove_student_button.grid(row=1, column=1, pady=10)

    close_button = tk.Button(remove_frame, text="Close Window", command=remove_window.destroy)
    close_button.grid(row=2, column=1, pady=30)


student_info = load_student_data("student-info.csv")

# Create a window
window = tk.Tk()
window.title("Student Manager")
window.geometry('600x400')
window.configure(bg='#333333')

# Add a frame on the window for responsiveness
frame = tk.Frame(window, bg="#333333", height=150, width=700)
frame.pack(pady=20, padx=50)

# Add and remove buttons linked to functions
add_button_student = tk.Button(frame, text="Add Student", width=30, command=add_student)
add_button_student.grid(row=1, column=1, pady=40)

remove_button_student = tk.Button(frame, text="Remove Student", width=30, command=remove_student)
remove_button_student.grid(row=2, column=1, pady=40)

window.mainloop()
