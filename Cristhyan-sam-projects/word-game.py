"""
List of words 
Get random words 
Inpute from user to quess the word
The longer the word the more trials allowed

To do
Quess the entire word when we have 1 left trial 
User functions 
Make the while loop false 
"""

import random


word_list = [
    "Python", "Project", "List", "Word", "Programming",
    "Code", "Variable", "Function", "Loop", "Condition",
    "Algorithm", "Data", "Structure", "Array", "String",
    "Integer", "Float", "Boolean", "Class", "Object",
    "Module", "Library", "Framework", "Variable", "Exception",
    "Debugging", "Testing", "Automation", "Documentation", "Comment",
    "Git", "Repository", "Commit", "Branch", "Merge",
    "Pull", "Push", "Remote", "Local", "Database",
    "SQL", "NoSQL", "Server", "Client", "API",
    "Endpoint", "Request", "Response", "Web", "HTML",
    "CSS", "JavaScript", "Frontend", "Backend", "Fullstack",
    "Design", "User", "Interface", "Responsive", "Mobile",
    "Desktop", "Database", "Schema", "Index", "Query",
    "Optimization", "Performance", "Security", "Authentication", "Authorization",
    "Encryption", "Decryption", "Agile", "Scrum", "Kanban",
    "Sprint", "Story", "Task", "Product", "Release",
    "Version", "Deployment", "DevOps", "Continuous", "Integration",
    "Deployment", "Delivery", "Docker", "Container", "Kubernetes",
    "Cloud", "AWS", "Azure", "GCP", "Virtualization",
    "Machine", "Learning", "Artificial", "Intelligence", "Automation"
]


secrect_word = word_list[random.randint(0,99)].lower()

print(f"The secret word has:{len(secrect_word)} letters")

user_guess = [' _ '] * len(secrect_word)

quantity_of_guesses = 5 if  len(secrect_word) <= 5 else 10 


correct_word = False
while True:
    print()
    guess = str(input("Enter guess letter: ").lower())

    if len(guess) > 1:
        print('Please enter only one letter')
        continue

    quantity_of_guesses -=1
    
    index = 0
    for letter in secrect_word: 
        if guess == letter:
            user_guess[index] = letter

        index +=1    

    print (' '.join(user_guess))

    if quantity_of_guesses == 0 and not correct_word:
        print ("You lost! The word was ", secrect_word)
        break

    elif user_guess == secrect_word:
        correct_word = False

        print("You Guessed Right")








