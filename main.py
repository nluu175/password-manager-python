from email.policy import default
import db_interaction
import sys
import utils

# Create a event loop here!
if __name__ == '__main__':
    currentUser = {"username": ""}
    print("| Welcome to Password Manager!")

    # connect.create_tables()

    while (currentUser["username"] == ""):
        msgs = ["| Please log in to use. ",
                "|  0. Sign In",
                "|  1. Sign Up",
                "|  2. Exit",
                "|---------------------------------------------------------------"]

        for msg in msgs:
            print(msg)

        choice = input("| Your choice = ? ")
        if int(choice) == 0:
            print("Sign In")
            while True:
                username = input("| Please enter your username: ")
                password = input("| Please enter your password: ")

                db_interaction.check_login(username, password)

        elif int(choice) == 1:
            print("|---------------------------------------------------------------")
            print("| Sign Up")

            username = input("| Please enter your username: ")
            while True:
                password = input("| Please enter your password: ")
                repeat_password = input("| Please re-enter your password: ")

                if password != repeat_password:
                    print("Passwords do not match. Try again!")
                    continue
                else:
                    break

            db_interaction.create_user(username, utils.hash_password(password))

        elif int(choice) == 2:
            sys.exit("Exiting ...")
            # https://www.geeksforgeeks.org/switch-case-in-python-replacement/

        else:
            print("|---------------------------------------------------------------")
            print("| Your input is wrong! Try again!")
            print("|---------------------------------------------------------------")
            continue

    while True:
        msgs = ["| What would you like to do? You can either: ",
                "|  0. Create a new password",
                "|  1. Get the already existing passwords",
                "|  2. Exit"]

        for msg in msgs:
            print(msg)

        choice = input("| Your choice = ? ")
        if int(choice) == 0:
            print("Enter the name for the password: ")

        elif int(choice) == 1:
            print("Here is a list of your passwords stored our system: ")

        elif int(choice) == 2:
            sys.exit("Exiting ...")

        else:
            print("|---------------------------------------------------------------")
            print("| Your input is wrong! Try again!")
            print("|---------------------------------------------------------------")
            continue
