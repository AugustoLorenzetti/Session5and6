name= input("What is your name?")
print("hello", name)
age = input("How old are you?")

try:
    age= int(age)
    new_age= age/0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("you can't divide by zero")
