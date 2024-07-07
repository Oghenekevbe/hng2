

# Django User Authentication & Organisation Management

## Overview
This project implements user authentication and organisation management using Django and Django Rest Framework (DRF). It allows users to register, log in, and manage organisations. Each user can belong to multiple organisations, and each organisation can have multiple users.

## Requirements

- Django
- django-rest-framework
- djangorestframework-simplejwt
- psycopg2
- python-decouple

## Setup

**Clone the repository:**
   ```
   git clone https://github.com/my-hng-internship-projects/hng2.git
   cd hng2
   ```
**Create and activate a virtual environment**


```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

```
**Install dependencies:**


```
pip install -r requirements.txt
```
**Set up environment variables:**

Create a .env file in the project root and add necessary environment variables:



```SECRET_KEY=your_secret_key
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
```

**Run migrations:**



```python manage.py migrate``` 

**Create a superuser:**



```python manage.py createsuperuser``` 

**Run the development server:**



```python manage.py runserver``` 

## API Endpoints
User Registration 

URL: /api/register/

Method: POST

Request Body:
```
json

{
  "email": "user@example.com",
  "password": "password123",
  "firstName": "John",
  "lastName": "Doe",
  "phone": "1234567890"
}

```
Response:
```
json

{
  "status": "success",
  "message": "Registration successful",
  "data": {
    "accessToken": "jwt_access_token",
    "user": {
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "phone": "1234567890"
    }
  }
}
```
User Login 

URL: /api/login/

Method: POST

Request Body:

```
json

{
  "email": "user@example.com",
  "password": "password123"
}
```
Response:
```
json

{
  "status": "success",
  "message": "Login successful",
  "data": {
    "accessToken": "jwt_access_token",
    "user": {
      "userId": "uuid",
      "firstName": "John",
      "lastName": "Doe",
      "email": "user@example.com",
      "phone": "1234567890"
    }
  }
}
``` 

User Details 

URL: /api/users/<uuid_str>/

Method: GET

Headers:
 

json

{
  "Authorization": "Bearer jwt_access_token"
} 

Response:
```
json

{
  "status": "success",
  "message": "User Retrieval Successful",
  "data": {
    "user": {
      "userId": "uuid",
      "firstName": "John",
      "lastName": "Doe",
      "email": "user@example.com",
      "phone": "1234567890"
    }
  }
}
```

User Organisations 

URL: /api/users/organisations/

Method: GET

Headers:
```
json

{
  "Authorization": "Bearer jwt_access_token"
}
```
Response:

```
json

{
  "status": "success",
  "message": "Organisations Retrieved Successfully",
  "data": {
    "organisations": [
      {
        "orgId": "uuid",
        "name": "Organisation Name",
        "description": "Organisation Description"
      }
    ]
  }
}

``` 

Create Organisation 

URL: /api/organisations/

Method: POST 


Headers: 

json

{
  "Authorization": "Bearer jwt_access_token"
} 

Request Body:
```
json

{
  "name": "New Organisation",
  "description": "Description of the new organisation"
}
```
Response:
```
json

{
  "status": "success",
  "message": "Organisation created successfully",
  "data": {
    "orgId": "uuid",
    "name": "New Organisation",
    "description": "Description of the new organisation"
  }
}
```
Organisation Details 

URL: /api/organisations/<uuid_str>/ 

Method: GET 

Headers: 

json

{
  "Authorization": "Bearer jwt_access_token"
} 

Response:
```
json

{
  "status": "success",
  "message": "Organisation Successfully retrieved",
  "data": {
    "orgId": "uuid",
    "name": "Organisation Name",
    "description": "Organisation Description"
  }
}
```
Add User to Organisation 

URL: /api/organisations/<orgId>/add-user/ 

Method: POST 

Headers: 

json

{
  "Authorization": "Bearer jwt_access_token"
} 

Request Body:
```
json

{
  "userId": "uuid"
}
```
Response:
```
json

{
  "status": "success",
  "message": "User added to organisation successfully"
}
```