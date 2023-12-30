import json
#VP Login Register With Python And JSON Code....


#the class that has the user information
class UserInformation:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
#function that registers a user and saves their info into JSON
def register_user(username, password):
    #we create a new user information
    new_user = UserInformation(username, password)
    #we open the json file in append mode
    with open("users.json", "a") as file:
       #creating a simple dictionary with the user data
        user_data = {"username": new_user.username, "password": new_user.password}
        #we write the user data into json
        json.dump(user_data, file)
        file.write("\n")  
#function that logins a user and loads their json info if the username and password match
def login(username, password):
    with open("users.json", "r") as file:
        for line in file:
            user_data = json.loads(line)
            if user_data["username"] == username and user_data["password"] == password:
                return True
    return False

while True:
    print("Welcome to the VP Login and Register with Python Application!")
    print("1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice:1,2,3: ")
    #if the choice is 1 we register a new user
    if choice == "1":
        registerUsername = input("Enter a new username: ")
        registerPassword = int(input("Enter a new password: "))
        register_user(registerUsername, registerPassword)
        print("Registration successful! "+"Welcome " +registerUsername)
        print("You can now register again or create a new account!")
     #if the choice is 2 we login a new user
    elif choice == "2":
        input_username = input("Enter your username: ")
        input_password = int(input("Enter your password: "))
        if login(input_username, input_password):
            print("Login successful! "+"Welcome "+ input_username)
            print("You can now register again or create a new account!")
        else:
            print("Username or password is not correct.")
   #if the choice is 3 we exit the application
    elif choice == "3":
        print("Exiting the application.")
        break
     #if the user pressed the wrong button 
    else:
        print("Please choose a correct number between 1,2 or 3.")