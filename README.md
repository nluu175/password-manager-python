# Password Manager 


## Why this?
- I want to make more secure passwords and also a place to store them as well. Normally, my password are stored in both the browser and icloud, but sometimes they lack the functionalities that I want.

## How to run this?
- Make sure to have PostgreSQL installed on your machine!
- Also, create a database with the name "password_manager"
- Create `config.py` with the template 
```
host=localhost
database=password_manager
user=<your_user>
password=<your_password>
```

- Create Python Virtual Environment using `python3 -m venv venv`
- Activate it using `source venv/bin/activate/`
- Install the packages using `pip install -r requirements.txt`
- You can deactiv-te the virtual env using `deactivate`

## TODO
- Allow auto generate password

- Store password by website

- Hash password? Choose a hash password method!!!

## Database Schema
- Check queries directory for more information.