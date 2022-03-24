#!/usr/bin/python
from connect import connect

# Create a event loop here!
if __name__ == '__main__':
    print("Welcome to Password Manager!")
    while True:
        user_input = input("What would you like to do? ")
        connect()
        break
