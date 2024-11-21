import getpass

import random

class Registration:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""

    def register(self):
        self.name = input("Welcome! Please enter your name: ")
        self.email = input("Enter your email: ")
        self.password = getpass.getpass("Enter your password: ")
        print(f"Registration successful! Hello, {self.name}!")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {'*' * len(self.password)}")

registration = Registration()
registration.register()
registration.display_details()


# Quiz data
quiz_data = {
    "Python": [
        {"question": "Who created Python?", "options": ["Guido van Rossum", "Bjarne Stroustrup", "Linus Torvalds", "Larry Wall"], "answer": "Guido van Rossum"},
        {"question": "What is the print function used for in Python?", "options": ["To display output", "To take input", "To store data", "To analyze data"], "answer": "To display output"},
        {"question": "What is the use of the len() function in Python?", "options": ["To calculate length", "To calculate size", "To calculate sum", "To calculate average"], "answer": "To calculate length"},
        {"question": "What is the use of the range() function in Python?", "options": ["To generate sequence", "To generate series", "To generate list", "To generate tuple"], "answer": "To generate sequence"},
        {"question": "What is the use of the list() function in Python?", "options": ["To generate sequence", "To generate series", "To generate list", "To generate tuple"], "answer": "To generate list"},
    ],
    "DBMS": [
        {"question": "What is DBMS?", "options": ["Database Management System", "Data Base Management System", "Database Management Services", "Data Base Management Services"], "answer": "Database Management System"},
        {"question": "Which DBMS is open-source?", "options": ["MySQL", "Oracle", "Microsoft SQL Server", "MongoDB"], "answer": "MySQL"},
        {"question": "What is normalization in DBMS?", "options": ["Process of organizing data", "Process of securing data", "Process of retrieving data", "Process of analyzing data"], "answer": "Process of organizing data"},
        {"question": "What is denormalization in DBMS?", "options": ["Process of organizing data", "Process of securing data", "Process of retrieving data", "Process of analyzing data"], "answer": "Process of analyzing data"},
        {"question": "What is indexing in DBMS?", "options": ["Process of organizing data", "Process of securing data", "Process of retrieving data", "Process of optimizing data"], "answer": "Process of optimizing data"},
    ],
    "DSA": [
        {"question": "What is DSA?", "options": ["Data Structure Algorithm", "Data Science Algorithm", "Database System Architecture", "Digital Signal Algorithm"], "answer": "Data Structure Algorithm"},
        {"question": "Which data structure is suitable for searching?", "options": ["Array", "Linked List", "Stack", "Hash Table"], "answer": "Hash Table"},
        {"question": "What is time complexity?", "options": ["Measure of space used", "Measure of time taken", "Measure of data used", "Measure of efficiency"], "answer": "Measure of time taken"},
        {"question": "What is space complexity?", "options": ["Measure of space used", "Measure of time taken", "Measure of data used", "Measure of efficiency"], "answer": "Measure of space used"},
        {"question": "What is Big-O notation?", "options": ["Measure of time complexity", "Measure of space complexity", "Measure of data complexity", "Measure of algorithm complexity"], "answer": "Measure of time complexity"},
    ]
} 

def quiz(subject):
    questions = quiz_data[subject]
    random.shuffle(questions)
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        answer_index = int(input("Enter answer number: ")) - 1
        if question["options"][answer_index] == question["answer"]:
            score += 1
    print(f"Your score is {score}/{len(questions)}")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Add authentication logic here
    return True

def main():
    if login():
        print("Login successful!")
        print("Select subject:")
        print("1. Python")
        print("2. DBMS")
        print("3. DSA")
        subject_choice = input("Enter subject number: ")
        subjects = {"1": "Python", "2": "DBMS", "3": "DSA"}
        subject = subjects[subject_choice]
        quiz(subject)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!")
        else:
            main()

if __name__ == "__main__":
    main()
