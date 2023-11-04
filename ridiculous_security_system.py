#list of known users
known_users = ["James", "Emma", "Michael", "Joseph", "Thomas", "Benjamin", "David", "Daniel", "Noah"]

#ask user for name and see whether they want to be added or removed
while True:
    print("Hello, I am a ridiculous security system.")
    name = input("What is your name?: ").strip().capitalize()
    
    if name in known_users:
        print(f"Hello, {name} I recognize you. Long time no see.")
        remove = input("Would you like to be removed from the security system (y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
            print("Sorry to see you go. Take care.")
        elif remove == "n":
            print("Awesome, I would have missed you.")
            
    else:
        print(f"Sorry, I do not recognize you {name}.")
        add_user = input("Would you like to be added to the security system (y/n)?: ").strip().lower()
        
        if add_user == "y":
            known_users.append(name)
            print("Your name has been added to the security system.")
        elif add_user == "n":
            print("No problem, maybe another time.")