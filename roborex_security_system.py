#list of known users
known_users = ["James", "Emma", "Michael", "Joseph", "Thomas", "Benjamin", "David", "Daniel", "Noah"]

#infinite loop to verify user has been added or removed
while True:
    print("----------------------------------------------")
    print("Hello, I am RoboRex, a humble security system.")
    name = input("\nWhat is your name?: ").strip().capitalize()
    
    #user's name is in known_users list
    if name in known_users: 
            print(f"\nHello, {name} I recognize you. Long time no see.")
            
            #while loop for user validation
            while True:
                remove_user = input("\nWould you like to be removed from the security system (y/n)?: ").strip()
                if remove_user == "y":
                    known_users.remove(name) #user is removed from known_users list
                    print("\nSorry to see you go. Take care.\n")
                    break
                elif remove_user == "n":
                    print("\nAwesome, I would have missed you.\n")
                    break
                else:
                    print("\nInvalid response, please enter 'y' or 'n' only.")
        
    #user's name is not in known_users list
    else:
        print(f"\nSorry, I do not recognize you {name}.")
        
        #while loop for user validation
        while True:
            add_user = input("\nWould you like to be added to the security system (y/n)?: ").strip()
            if add_user == "y":
                known_users.append(name) #user is added to known_users list
                print("\nYour name has been added to the security system.\n")
                break
            elif add_user == "n":
                print("\nNo problem, maybe another time.\n")
                break
            else:
                print("\nInvalid response, please enter 'y' or 'n' only.")