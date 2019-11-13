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

## FOLDERS AND FILES
```
|--models:
	|--engine:
		|--__init__.py     #empty file
		|--file_storage    #FileStorage class with __init__, all, new, save and reload methos
        |--__init__.py      #init file for the module
        |--amenity.py       #Amenity(BaseModel) class with public attributes
	|--base_model.py    #BaseModel super class with save, to_dict, __str__ and __init__ methods 
	|--city.py          #City(BaseModel) class with public attributes state_id and name
	|--place.py         #Place(BaseModel) class with puclic attributes city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude and amenity_ids
	|--review.py        #Review(BaseModel) class with public attributes place_id, user_id and text
	|--state.py         #State(BaseModel) class with public attributes name
	|--user.py          #User(BaseModel) class with public attributes email, password, first_name and last_name.
|--tests:
	|--test_models:
		|--test_engine:
			|--__init__.py              #empty file
			|--test_file_storage.py     #test for FileStorage class
		|--__init__.py           #
		|--test_amenity.py       #test for Amenity class
		|--test_base_model.py    #test for BaseModel class
		|--test_city.py          #test for City class
		|--test_place.py         #test for Place class
		|--test_review.py        #test for Review class
		|--test_state.py         #test for State class
		|--test_user.py          #test for User class
	|--__init__.py    #empty file
|--.gitignore             #for github ignore extentions files
|--AUTHORS                #who write the code in this project
|--README.MD              #file with general description about this project
|--console.py             #Making the console with the clas HBNBCommand and implement the commands: show, create, quit, Ctrl + d, destroy, all, update and emptyline
```