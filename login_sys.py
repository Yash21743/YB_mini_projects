def signup():
    username=input("Enter new username -->  ")
    password=input("Enter 🔒 new password --> ")


#check if username already exists...
    with open("users.txt","r") as file:
        for line in file:
            stored_username, _ =line.strip().split(",")
            if username == stored_username:
                print("Username already exists...Try again...")
                return   

#save  new user....
    with open("users.txt","a") as file:
        file.write(f"{username},{password}\n")
    print(" 🛡️ Signup Succesfull....")


def login():
    username=input("Enter  username -->  ")
    password=input("Enter 🔒 password --> ")


#check if username already exists...
    with open("users.txt","r") as file:
        for line in file:
            stored_username, stored_password =line.strip().split(",")
            if username == stored_username and password == stored_password:
                print(f"Login Succesfull! Welcome {username}")
                return   
    print("Invalid username or password...")


def main():
    while True:
        print("\n____Welcome to Login System____")
        print("1. signup")
        print("2. login")
        print("3. Exit")
        choice=input("Enter choice --> (1/2/3): ")
        
        if choice== '1':
            signup()
        elif choice == '2':
            login()
        elif choice== '3':
            print("Exit 🚪 Program...")
            break
        else:
            print("Invalid Input. Try again....")

#Run the programe...
if __name__ == "__main__":
    open("users.txt","a").close()
    main()
