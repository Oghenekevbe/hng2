# Django Person API

This is a simple Django REST API for managing person records. It allows you to perform CRUD (Create, Read, Update, Delete) operations on person data.

## Installation

- Clone this repository to your local machine.



  '''sh

  git clone <repository_url>
'''
- Navigate to the project directory.



- cd django-person-api
- Create a virtual environment (optional but recommended).

'''sh
python -m venv venv
'''
- Activate the virtual environment.

**On Windows**:


> venv\Scripts\activate
**On macOS and Linux**:



> source venv/bin/activate
> Install project dependencies.

- pip install -r requirements.txt
- Run the development server.


- python manage.py runserver
The API will be available at http://localhost:8000/api.

## Usage
_Get a List of Persons_
To get a list of all persons, make a GET request to:



> http://localhost:8000/api
_Get a Person_
 Note that you can get a person either by id or by name.

_Get a Person by ID_
To retrieve a person by their ID, make a GET request to:



> http://localhost:8000/api/user_id
_Get a Person by Name_
To retrieve a person by their name, make a GET request to:



> http://localhost:8000/api/name
_Create a New Person_
To create a new person, make a POST request to:



> http://localhost:8000/api
Include the person's data in the request body in JSON format.

_Update a Person_
To update an existing person, make a PUT request to:



> http://localhost:8000/api/<user_id>
Replace <user_id> with the ID of the person you want to update. Include the updated data in the request body in JSON format.

_Delete a Person_
To delete a person, make a DELETE request to:



> http://localhost:8000/api/<user_id>
Replace <user_id> with the ID of the person you want to delete.




