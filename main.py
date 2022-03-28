from email.policy import default
from connect import connect
import sys

# Create a event loop here!
if __name__ == '__main__':
    print("Welcome to Password Manager!")
    print("|---------------------------------------------------------------")
    while True:
        # TODO: Can have a checkpoint for each question for comming back on invalid input
        # Each checkpoint can be indexed and assigned a function
        msgs = ["| What would you like to do? You can either: ",
                "|  0. Create a new password",
                "|  1. Get the already exists password",
                "|  2. Exit"]
        for msg in msgs:
            print(msg)
        choice = input("Your choice = ? ")
        if int(choice) == 0:
            print("Enter the name for the password: ")

        elif int(choice) == 1:
            print("Here is a list of your passwords stored our system: ")

        elif int(choice) == 2:
            sys.exit("Exiting ...")
            # https://www.geeksforgeeks.org/switch-case-in-python-replacement/
            # connect()

        else:
            print("| Your input is wrong! Try again!")
            continue
