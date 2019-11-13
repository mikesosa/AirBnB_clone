<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# AirBnb clone - The console
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function                                   
## Examples                                                                     
EXAMPLE 1:

```
The input:

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
```
The output is:
```
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427from models.base_model import BaseModel
```
for more information see the file: models/base_model.py

EXAMPLE 2:

The input:
program that contains the entry point of the command interpreter:

The output:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
```
for more information see the file console.py
## Prerequisites

knowledge in python3:
- Tuples
- Strings
- Dictionaries(in this project is so important)
- Methods
- Classes
- Unittest
- __init__ files
- Libraries(os, shlex, unittest, uuid, datatime, json)
- *args and **kargs
- Serialization/deserealization in JSON
- Docstrings
- pep8

## Installing
You can fork/clone the repository and run it in your pc, you need python3.
## Built With
- Python 3.4.3
- pep8
## Contributing

-- Michael Sos - Holberton Student                                              
-- Yesid Gutierrez - Holberton Student                                          

## Versioning

This project was developed like a part for a full AirBnb clone using python.
this is the first version V.0.0 for Holberton peer learning.

## Authors

---Michael Sosa  833@holbertonschool.com                                      
---Yesid Gutierrez  944@holbertonshcool.com                                    

## Projects

|                          Project                      |              Description                 |
| ----------------------------------------------------- | ---------------------------------------- |
