from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user1 =User(name="Gova", age=41)
print(user1)

#Automatic type conversion testing
user2 = User(name = "Isha", age = '7')
print(user2)
print(type(user2.age))

#Even though '7' was a string, Pydantic converted it to int.
# This is called data parsing.

#Validation errors
user3 = User(name = "Chitti", age = "30")
print(user3)

# Here user3 = User(name = "Chitti", age = "Thirty") was throwing error and not executing rest of the code.
# validation error for User age
# Input should be a valid integer, unable to parse string as an integer
# Pydantic stops bad data early

# Default values
class Client(BaseModel):
    name: str
    age: int
    country: str = "USA"

client1 = Client(name = "Tester", age = 35)
print(client1)
#  Optional fields
