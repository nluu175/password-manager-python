import bcrypt
import string
import random


def password_generator(length):
    """
    Password should
    - be at least 8 characters long.
    - include symbols
    - include numbers 
    - include lowercase characters
    - include uppercase characters
    """
    # Currently the password is not guaranteed to have all of these requirements
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()"
    all_chars = letters + digits + symbols

    pre_pwd = random.sample(all_chars, length)

    return "".join(pre_pwd)


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')
