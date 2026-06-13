import sys
name = input("What is your name?: ")
role = input("What is your role?: ")
def greeting(name, role):
    print(f"Welcome {name}! Your role is {role}.")
    print("Python version:",sys.version)

greeting(name,role)