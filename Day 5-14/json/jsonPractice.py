# The four important JSON functions
import json
from pathlib import Path


# json.dumps()
# Converts a Python object into a JSON string.

""" 

obj={
    'name':"Indrajit barui",
    "age":21,
    "height":5.6,
    "course": "BCA",
    "is_student": True,
    "marks": None
}

result=json.dumps(obj)
print(type(result))
print(result)

"""
# json.dump()-> Write a Python into a JSON file.


"""
student = {
    "name": "Akash",
    "age": 21,
    "skills": ["python", "js", "cpp"]
}

file_path = Path(__file__).parent / "student.json"

with open(file_path, "w") as file:
    json.dump(student, file, indent=4)

print("File created successfully!")
""" 

#json.load()-> read json data from a file

with open("student.json","r") as file:
    result=json.load(file)
    
print(result)
print(type(result))

# json.loads()  -> Convert a JSON string into a python object

import json

data = '''         
{
    "name": "Indrajit",
    "age": 21,
    "course": "BCA"
}
'''

result = json.loads(data)

print(result)
print(type(result))
