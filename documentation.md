# Introduction
[google]

This API provides **CRUD (Create, Read, Update, Delete) operations** for managing person records. You can interact with this API to add, retrieve, update, and delete person information.

To access the API, use the base URL: [https://your-domain.com/api/].

## Endpoints
**Get a Person**
Request

[URL: /api or /api/<str:name>]
**Method: GET**
**Description**: Get a list of all persons or retrieve a specific person by name or primary key (pk).
Parameters

name (optional): Filter persons by name.
pk (optional): Retrieve a person by their primary key (pk).
Example

Get a list of all persons:



GET https://your-domain.com/api/
Retrieve a specific person by name (replace <name> with the desired name):



GET https://your-domain.com/api/<str:name>
Retrieve a specific person by primary key (replace <pk> with the desired primary key):



GET https://your-domain.com/api/<int:pk>
```sh
Response

Status Code: 200 OK
Body: A JSON array containing person records.
Example Response



[
  {
    "id": 1,
    "name": "John Doe",
    "bio": "A software developer."
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "bio": "An engineer."
  }
]

```

Create a Person
Request

URL: /api/
**Method: POST**
**Description**: Create a new person record.
Parameters

name (required): The name of the person.
bio (required): The biography or description of the person.
Example

**Create a new person**:



POST https://your-domain.com/api/
Content-Type: application/json

```sh
{
  "name": "John Doe",
  "bio": "A software developer."
}
Response

Status Code: 201 Created
```
Body: A JSON object containing the created person record.
Example Response


```sh

{
  "id": 1,
  "name": "John Doe",
  "bio": "A software developer."
}


```
**Update a Person**
Request

URL: /api/<str:name> or /api/<int:pk>
**Method: PUT**
**Description**: Update an existing person record by specifying the person's name or primary key (pk).
Parameters

name (optional): The name of the person (in the URL).
pk (optional): The primary key (pk) of the person (in the URL).
bio (required): The updated biography or description of the person.
Example

Update a person by name (replace <name> with the person's name):



PUT https://your-domain.com/api/<str:name>
Content-Type: application/json

```sh
{
  "bio": "An experienced software developer."
}
```
Update a person by primary key (replace <pk> with the person's primary key):



PUT https://your-domain.com/api/<int:pk>
Content-Type: application/json

```sh
{
  "bio": "An experienced software developer."
}
Response

Status Code: 200 OK
```
Body: A JSON object containing the updated person record.
Example Response


```sh
{
  "id": 1,
  "name": "John Doe",
  "bio": "An experienced software developer."
}
```


**Delete a Person**
Request

URL: /api/<str:name> or /api/<int:pk>
**Method: DELETE**
**Description**: Delete an existing person record by specifying the person's name or primary key (pk).
Example

Delete a person by name (replace <name> with the person's name):



DELETE https://your-domain.com/api/<str:name>
Delete a person by primary key (replace <pk> with the person's primary key):



DELETE https://your-domain.com/api/<int:pk>
Response

Status:
404 Not Found (if the person with the given ID or name is not found)
204 No Content (if the person is successfully deleted)
Request and Response Formats
All API requests and responses use the JSON format.

## Setup Instructions
To set up and run this API locally, follow these steps:

- Clone the project from the GitHub repository.
- Install the required dependencies using pip install -r requirements.txt.
- Run the Django development server using python manage.py runserver.

### Sample API Usage
Here are some sample API usage scenarios:

- To retrieve all persons: Send a GET request to /api.
- To create a new person: Send a POST request to /api with the person's details in the request body.
- To update a person: Send a PUT request to /api/user_id with the person's ID or person's name in the URL and updated details in the request body.
- To delete a person: Send a DELETE request to /api/user_id with the person's ID in the URL.


### Known Limitations
This API does not support pagination for large datasets.
Deleting a person with associated data (e.g., related records) may not be supported.
Contact Information
For any questions or issues related to this API, please contact Oghenekevbe at oghenekevbe.egume@gmail.com.
