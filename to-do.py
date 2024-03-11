import tkinter as tk

"""
This is a To do list manager . You can add tasks, mark them done and delete them. 

1. create a window  for the application using Tkinter library.
2. Create an empty list to store all the tasks.
3. Create a text widget where you will enter your task.
4. A button that when clicked , adds the current content of the text widget into the list.
5. Another button which displays all the tasks in the list on the console.
6. A checkbutton next to each task which allows user to mark it as done or not.
7. A clear button which clears out everything from the list.
8. Add functionality so that if the checkbox is checked then print "Done : Task" else just print "Task".
9. If there are no tasks left in the list , display a message saying "No Tasks Left!"

Use as many resuable functions as  possible.
"""

tast_list = []

def add_task():

    new_task = input ("Enter Your Task: ")
    tast_list.append(new_task)

    






def main():
    #create window
    window = tk.Tk()
    window.title("To Do Manager")
    window.geometry("600x400")
    window.configure (bg='#fafafa')

    #add frame
    frame = tk.Frame(window, bg="#333333" ,height=700, width=700) 
    frame.pack(pady=20, padx= 50)


    
    window.mainloop()

if __name__ == "__main__":
    main()  



