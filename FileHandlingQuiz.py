import random

def register():
    name = input("Enter a username: ")
    with open("users.txt", "r") as file:
        users = {}
        for line in file:
            if ":" in line:  
                user, pwd = line.strip().split(":", 1)
                users[user] = pwd
    if name in users:
        print("User already exists!")
        return False
    pwd = input("Enter a password: ")
    with open("users.txt", "a") as file:
        file.write(f"{name}:{pwd}\n")
    print("Registration successful!")
    return True

def login():
    name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    with open("users.txt", "r") as file:
        users = {}
        for line in file:
            if ":" in line:  
                user, stored_pwd = line.strip().split(":", 1)
                users[user] = stored_pwd
    if users.get(name) == pwd:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

quiz_data = {
    "C++": [
        {"q": "Which of these is a valid C++ data type?", "o": ["int", "float", "bool", "All of these"], "a": "All of these"},
        {"q": "What is the correct file extension for C++ files?", "o": [".c", ".cpp", ".py", ".java"], "a": ".cpp"},
        {"q": "Which operator is used to access a pointer in C++?", "o": ["*", "&", "->", "%"], "a": "->"},
        {"q": "Which keyword is used to declare a class in C++?", "o": ["struct", "class", "define", "type"], "a": "class"},
        {"q": "Which of these is not a loop in C++?", "o": ["for", "do-while", "until", "while"], "a": "until"},
    ],
    "Python": [
        {"q": "Which keyword is used to define a function in Python?", "o": ["func", "def", "function", "define"], "a": "def"},
        {"q": "How do you create a list in Python?", "o": ["[]", "{}", "()", "<>"], "a": "[]"},
        {"q": "Which library is used for data analysis?", "o": ["numpy", "pandas", "math", "os"], "a": "pandas"},
        {"q": "What is used to install packages in Python?", "o": ["pip", "npm", "brew", "apt"], "a": "pip"},
        {"q": "Which function converts a string to an integer?", "o": ["str()", "int()", "float()", "convert()"], "a": "int()"},
    ],
    "DSA": [
        {"q": "Which data structure uses FIFO?", "o": ["Queue", "Stack", "Array", "Tree"], "a": "Queue"},
        {"q": "Which algorithm is used for sorting?", "o": ["Merge Sort", "Binary Search", "DFS", "BFS"], "a": "Merge Sort"},
        {"q": "Which data structure is a LIFO?", "o": ["Queue", "Stack", "Array", "Graph"], "a": "Stack"},
        {"q": "What is the time complexity of binary search?", "o": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": "O(log n)"},
        {"q": "Which traversal is used in binary trees?", "o": ["Inorder", "Preorder", "Postorder", "All of these"], "a": "All of these"},
    ]
}

def quiz(subject, user):
    print(f"\nStarting {subject} quiz!")
    score = 0
    questions = random.sample(quiz_data[subject], len(quiz_data[subject]))[:5]
    
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q['o'], 1):
            print(f"{idx}. {option}")
        ans = input("Your answer (1/2/3/4): ")

        if q['o'][int(ans) - 1] == q['a']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['a']}")
    
    print(f"\n{user}, your score is {score}/5.")

def main():
    try:
        open("users.txt", "x").close()
    except FileExistsError:
        pass

    print("Welcome to the Quiz Application!")
    user = None

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            user = login()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    while True:
        print("\nSubjects:\n1. C++\n2. Python\n3. DSA")
        choice = input("Choose a subject (1-3): ")
        if choice == "1":
            quiz("C++", user)
        elif choice == "2":
            quiz("Python", user)
        elif choice == "3":
            quiz("DSA", user)
        else:
            print("Invalid choice!")
            continue

        play_again = input("Do you want to take another quiz? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

