from connect import connect

# Create a event loop here!
if __name__ == '__main__':
    print("Welcome to Password Manager!")
    print("|---------------------------------------------------------------")
    while True:
        msgs = ["| What would you like to do? You can either: ",
                "|  1. Create a new password",
                "|  2. Get the already exists password",
                "|  3. Exit"]
        for msg in msgs:
            print(msg)
        choice = input("Your choice = ? ")
        # https://www.geeksforgeeks.org/switch-case-in-python-replacement/
        # connect()https://www.geeksforgeeks.org/switch-case-in-python-replacement/
        break
