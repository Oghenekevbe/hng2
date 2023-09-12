Person API Documentation
Introduction
This API allows you to perform CRUD (Create, Read, Update, Delete) operations on a "Person" resource. You can create, retrieve, update, and delete person records based on their name or age.

API Endpoints
Get Person(s)
Endpoint: /api
Method: GET
Description: Retrieve person records based on optional query parameters (name or age). If no parameters are provided, all person records will be returned.
Request Parameters:
name (optional): Filter persons by name.
age (optional): Filter persons by age.
Response:
Status: 200 OK
Body (example):


[
	{
		"id": 2,
		"name": "Christina",
		"age": 38,
		"bio": "Head of Cardio"
	},
	{
		"id": 3,
		"name": "Meredith",
		"age": 32,
		"bio": "Head of General Surgery"
	}
]
Create a New Person
Endpoint: /api
Method: POST
Description: Create a new person record.
Request Body:


{
  "name": "John Doe",
  "age": 30,
  "bio": "This is a bio example"
}
Response:
Status: 201 Created
Body (example):


{
  "message": "Person created successfully",
  "data": {
    "id": 3,
    "name": "John Doe",
    "age": 30,
    "bio": "This is a bio example"
  }
}
Update a Person
Endpoint: /api/user_id
Method: PUT
Description: Update an existing person record by providing its ID. You can also filter persons by name or age.
Request Parameters:
id: ID of the person to update.
Request Body:


{
  "name": "Updated Name",
  "age": 35,
  "bio": "updated bio"
}
Response:
Status: 200 OK
Body (example):


{
  "message": "Person instance updated successfully",
  "data": {
    "id": 1,
    "name": "Updated Name",
    "age": 35,
    "bio": "updated bio"
  }
}
Delete a Person
Endpoint: /api/user_id
Method: DELETE
Description: Delete a person record by providing its ID. You can also filter persons by name.
Request Parameters:
id: ID of the person to delete.
Response:
Status: 404 Not Found (if the person with the given ID or name is not found)
Status: 204 No Content (if the person is successfully deleted)
Request and Response Formats
All API requests and responses use the JSON format.

Setup Instructions
To set up and run this API locally, follow these steps:

Clone the project from the GitHub repository.
Install the required dependencies using pip install -r requirements.txt.
Run the Django development server using python manage.py runserver.
Sample API Usage
Here are some sample API usage scenarios:

To retrieve all persons: Send a GET request to /api
To create a new person: Send a POST request to /api with the person's details in the request body.
To update a person: Send a PUT request to /api/user_id with the person's ID in the URL and updated details in the request body.
To delete a person: Send a DELETE request to /api/user_id with the person's ID in the URL.
Known Limitations
This API does not support pagination for large datasets.
Deleting a person with associated data (e.g., related records) may not be supported.
Contact Information
For any questions or issues related to this API, please contact Oghenekevbe at ighenekevbe.egume@gmail.com.