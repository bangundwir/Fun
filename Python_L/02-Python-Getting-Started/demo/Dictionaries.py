# # Dictionaries
# student = {
#     "name": "Puguh",
#     "student_id":1234,
#     "feedback":None
# }

# # List of Dictionaries
# all_students = [
#         {"name":"Puguh","student_id":1234 },
#         {"name":"Joko","student_id":5234 },
#         {"name":"Thalia","student_id":1231 }
# ]


# Dictionary Data
student["name"] == "Puguh"
student["last_name"] == KeyError
student.get("last_name", "Unknown") == "Unknown"
student.keys() = ['name','student_id', 'feedback']
student.values() = ['Puguh', 1234, None]
student["name"] = "Joko"
del student["name"]
