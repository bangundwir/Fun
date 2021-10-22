# Exceptions

# Dictionaries
student = {
    "name": "Puguh",
    "student_id":1234,
    "feedback":None
}


# last_name = student["last_name"] # Error

# try:
#     last_name = student["last_name"]
# except KeyError:
#     print("Error finding last_name")
# print("This code executes!")

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)
print("This code executes!")
