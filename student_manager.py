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

    # This function is called when the add button is clicked to add student to file
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

            print(f"Student added: {new_student}")

            # Call the write student function
            write_to_file("student-info.csv", student_info, heading)

            messagebox.showinfo("Success!", "New student added successfully.")

            # Close the add window
            add_window.destroy()

    
    #create lables and entry boxes for GUI
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


#this function should update students info
#It is not working yet
"""
  
def update_student():
    # Create a window to update student info
    update_student_window = tk.Toplevel()
    update_student_window.title("Update student")
    update_student_window.geometry('600x400')
    update_student_window.configure(bg='#333333')

    # Add a frame
    update_student_frame = tk.Frame(update_student_window, bg="#333333", height=150, width=700)
    update_student_frame.pack(pady=20, padx=50)

    id_var = tk.StringVar()
    new_id_var = tk.StringVar()
    new_name_var = tk.StringVar()
    new_classes_var = tk.StringVar()
    new_cost_var = tk.StringVar()

    def search_and_update():
        global student_info

        id_value = id_var.get()

        for student in student_info:
            if student[0] == id_value or student[1] == id_value:
                # Display current information
                messagebox.showinfo("Current Information", f"ID: {student[0]}\nName: {student[1]}\nClasses: {student[2]}\nCost: {student[3]}")

                # Ask for new information
                new_id = new_id_var.get()
                new_name = new_name_var.get()
                new_classes = new_classes_var.get()
                new_cost = new_cost_var.get()

                # Update student information
                student[0] = new_id
                student[1] = new_name
                student[2] = new_classes
                student[3] = new_cost

                # Save the updated information to the file
                write_to_file("student-info.csv", student_info, heading=None)

                messagebox.showinfo("Success!", "Student information updated successfully.")
                update_student_window.destroy()
                return

        # If student not found
        messagebox.showwarning("Warning", "Student not found.")



        id_label = tk.Label(update_student_frame, text="ID number:")
        id_label.grid(row=0, column=0, pady=15)
        id_entry = tk.Entry(update_student_frame, textvariable=id_var)
        id_entry.grid(row=0, column=1, pady=15)

        new_id_label = tk.Label(update_student_frame, text="New Student ID:")
        new_id_label.grid(row=1, column=0, pady=15)
        new_id_entry = tk.Entry(update_student_frame, textvariable=new_id_var)
        new_id_entry.grid(row=1, column=1, pady=15)

        new_name_label = tk.Label(update_student_frame, text="New Name:")
        new_name_label.grid(row=2, column=0, pady=15)
        new_name_entry = tk.Entry(update_student_frame, textvariable=new_name_var)
        new_name_entry.grid(row=2, column=1, pady=15)

        new_class_label = tk.Label(update_student_frame, text="New Number of Classes:")
        new_class_label.grid(row=3, column=0, pady=15)
        new_class_entry = tk.Entry(update_student_frame, textvariable=new_classes_var)
        new_class_entry.grid(row=3, column=1, pady=15)

        new_cost_label = tk.Label(update_student_frame, text="New Cost per Class: $")
        new_cost_label.grid(row=4, column=0, pady=15)
        new_cost_entry = tk.Entry(update_student_frame, textvariable=new_cost_var)
        new_cost_entry.grid(row=4, column=1, pady=15)

        update_button = tk.Button(update_student_frame, text='Update', command=search_and_update)
        update_button.grid(row=5, column=1, pady=15)
"""  

# This function loads students info from file
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

student_info = load_student_data("student-info.csv")


# This function removes a student from the csv file
def remove_student():
    remove_window = tk.Toplevel()
    remove_window.title("Remove Student")
    remove_window.geometry('600x400')
    remove_window.configure(bg='#333333')

    # Add a frame
    remove_frame = tk.Frame(remove_window, bg="#333333", height=150, width=700)
    remove_frame.pack(pady=20, padx=50)

    # Create variable for the id entry
    id_var = tk.StringVar()

    # This function is called when the remove student button is clicked
    def remove_from_database():
        global student_info  

        # Get the ID value from the entry
        id_value = id_var.get()

        # Check if the student with the specified ID exists
        if any(student[0] == id_value for student in load_student_data("student-info.csv")):

            # Confirm that you want to delete
            confirmation = messagebox.askyesno("Confirm Removal", f"Are you sure you want to delete student with ID {id_value}")

            if confirmation:
                # Remove the student with the specified ID
                student_info = [student for student in student_info if student[0] != id_value]

                # Call the write student function to update the file
                write_to_file("student-info.csv", student_info, heading)

                messagebox.showinfo("Success!", f"Student with ID {id_value} removed successfully.")
            else:
                messagebox.showwarning("Warning", "Deletion canceled.")
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




def get_student():
    get_window = tk.Toplevel()
    get_window.title("Get Student")
    get_window.geometry('600x400')
    get_window.configure(bg='#333333')

    get_student_frame = tk.Frame(get_window, bg="#333333", height=150, width=700)
    get_student_frame.pack(pady=20, padx=50)

    id_var = tk.StringVar()

    def search_for_student():
        try:
            identifier_value = id_var.get()
            found_student = None

            for student in student_info:
                if str(identifier_value) in [student[0], student[1]]:
                    found_student = student
                    break

            if found_student:
                message = "\nID: " + found_student[0] + "\nName: " + found_student[1] + "\nNo of Classes: " + str(found_student[2]) + "\nCost per class: $" + str(found_student[3])
                messagebox.showinfo("Success! Student found", message)
                #close the window
                get_window.destroy()

            else:
                messagebox.showerror("Error! Student not found.")
        except Exception as e:
            messagebox.showerror("Error! An unexpected error occurred")
        
            #close the window
            get_window.destroy()

    # Add widgets for the get student window
    id_label = tk.Label(get_student_frame, text="Student ID:")
    id_label.grid(row=0, column=0, pady=15)
    id_entry = tk.Entry(get_student_frame, textvariable=id_var)
    id_entry.grid(row=0, column=1, pady=15)

    search_button = tk.Button(get_student_frame, text="Search", command=search_for_student)
    search_button.grid(row=1, column=1)




#this function computes the cost of classes per month
def compute_cost():

    compute_cost_window = tk.Toplevel()
    compute_cost_window.title("Calculate fees")
    compute_cost_window.geometry('600x400')
    compute_cost_window.configure(bg='#333333')

    cost_frame = tk.Frame(compute_cost_window, bg='#333333')
    cost_frame.pack(pady=40)

    student_var = tk.StringVar()
    cost_var = tk.StringVar()

    def calculate():
        identifier = student_var.get()
        found_student = None

        for student in student_info:
            if student[0] == identifier:
                found_student = student
                break

        if found_student:
            No_of_classes = int(found_student[2])
            cost_per_class = float(found_student[3])
            cost_per_month = No_of_classes * cost_per_class * 4

            #messagebox.showinfo(cost_per_month) - finish displaying cost in a message box later

            cost_var.set(f"cost Per Month: {cost_per_month}")
            return cost_per_month

           
        else:
            return None

    # Add widgets for the compute cost window
    id_label = tk.Label(cost_frame, text="Student ID:")
    id_label.grid(row=0, column=0, pady=15, padx=10)

    id_entry = tk.Entry(cost_frame, textvariable=student_var)
    id_entry.grid(row=0, column=1, pady=15, padx=10)

    compute_button = tk.Button(cost_frame, text="Compute Cost", command=calculate)
    compute_button.grid(row=1, column=1, pady=15)

    result_label = tk.Label(cost_frame, textvariable= cost_var)
    result_label.grid(row=2, column=0, pady=15)




def  main():

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
    add_button_student.grid(row=1, column=1, pady=20)

    remove_button_student = tk.Button(frame, text="Remove Student", width=30, command=remove_student)
    remove_button_student.grid(row=2, column=1, pady=20)

    get_button_student = tk.Button(frame, text="Get Student Information", width=30, command=get_student)
    get_button_student.grid(row=3, column=1, pady=20)

    compute_class_cost= tk.Button(frame, text="Compute Class Cost", width=30, command=compute_cost)
    compute_class_cost.grid(row=4, column=1, pady=20)

    update_student_window = tk.Button(frame, text= "Update Student", width=30, command=update_student)
    update_student_window.grid(row=5,column=1,pady=20)


    window.mainloop()

if __name__ == "__main__":
    main()  
