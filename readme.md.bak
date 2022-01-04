# Casting Agency Project

This project is about company that is responsible for creating movies and managing and assigning actors to those movies.

Following roles and functionalities have been implemented as part of this project:

1. Casting assistant: who can view actors and movies and has limited access.
2. Casting director: who can view and edit actors and movies, also create and delete actors, has limited access to movies.
3. Executive producer: who has all the accesses to view, edit, create and delete actors and movies.

## Casting Agency Project

This project helps gain better understanding of all the concepts learned throughout the course and allowed me to implement the knowledge I gathered.

## Setting up project locally

### Dependencies
Developers should have Python3, pip, flask, node, and npm installed.

### Set up environment and install requirements

Setup a virtual environment as this keeps your dependencies for each project separate and organized. Then install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

### Setup database

1. Start your postgres server and update database path in models
2. Create a db and add dummy data

### Auth0 cnfiguration

Update Auth0 params in auth file, following params have been used for the project:

```bash
AUTH0_DOMAIN = 'dev-jdd6v-si.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'castingagency'
```

### Running the app locally

Execute commands:

```bash
export FLASK_APP=app.py
flask run
```

### Testing

To run the tests, run

```bash
python test_app.py
```

## Auth0 details:

1. Domain - dev-jdd6v-si.us.auth0.com
	
2. Client Id - z9n4IAz9fX4I0QYcKdgIzAvuZhJhW1ty

## Heroku deployment

Project is hosted via heroku, link: https://casting-agency19.herokuapp.com/

## Access tokens

* Casting assistant access token:
	
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwYzBlMDljODMwMDZmMWIyMjQ2IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTI3MDg0MiwiZXhwIjoxNjQxMjc4MDQyLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.CTa37ROFelB-XTpmlHGoSm5dEzA-FGavjtByM4o0z89BsrHcikiFftWubJdrCG7BTgGq7UctNvyTRHdzmyzr9jOHGyq_JM59SAQvzhi-TgLGTZHuBl3Z9wUauGOmkLUa1-ITkdULpoAogSe9bdQtpzZDI06Y1Lywrg4liomTPdIfodvJex6gbyuw5hNhQUt8E87BWs0gY9C3ydG-I_rJHsXnD68GUWJ3YZhky2e-1azwNXscm6YHoDctpYdpHNfKwhaFs7P0Pj4gh97topJl2ilCOp5-FrMzxQrd0BbiA9ODwvQ2IdOosz-N5EkjQ67HAjPr3RMQMLFi_P2-54av4g
	
* Casting director access token:
	
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwOTRmYTJjZDEwMDY5ZWU2Mjc5IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTI3MDgyNywiZXhwIjoxNjQxMjc4MDI3LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.FPQ7_MVDInqgFF6X9HlHUa1sQJAxb3kaEB1JS5j6Nla-pRIE5Xv1Y9zdj1eRkALFSbSUAdR3PtGGkT4rX0HkgmXgdLl3cggOMwYTKaih2Amjl8v7sSVqGMLuvNmZcZSx7m8GUAmzlPdc6HbZqHySB-H2iauFuTaPbKcUEbstcFYjZ-wtC-Tul8GaUiQoXi-k3cy4hF-uhWLx4Xqi9oa1xVrDKClV1tgkLVv4VWsHT-d47qZDhGXDbdChEP0iHOT8EFQd3LQ74LXMoD--Zq5XrXXUV8JBb3rnlJsF92yosaax9k2Co2QkzX3teBmWQsX3S9FCSYMWcaXdnlW1p3xgKA
	
* Executive producer access token:
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwNWZmYTJjZDEwMDY5ZWU2MjZlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTI3MDgxOCwiZXhwIjoxNjQxMjc4MDE4LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.Z7leh7gCbsmo1idYaI-13xGmaI9JUZqn9W4ODcHlp16vlHWiIqVAf5t4sXgMUeFLiQg72Mooh7BHWH49U1U6BjawPE9lPUNyWkQAeo_UPyMBwdGt34nA9HgYiUf3INUJ2-fpzvotZE_wTUa5IyBEiKy-Q1j2ZZnLpjtmxIHgSpGp9pypabNHe0k6J0JHUHRz_tz-Q3CPanf5753ZwmXvjCIUEEmfKTV74BMnp4HvKJVjyJs_Cl1rtxjG0tfHz2BzGGWz79Kifr6yjHxA7rJVJRZSGoI9RcLOR4xb4XjEBNr1N5CmXBp5QWtXbly5KfeBRRehldv7AEgQh04XAvtuAg

## API Reference

### Getting Started

### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return four types of errors:

* 400 – bad request
* 401 - unauthorized
* 404 – resource not found
* 422 – unprocessable

### Endpoints

#### GET /actors

* General: Retrieves actors
* Sample: `curl https://casting-agency19.herokuapp.com/actors -H "Authorization: Bearer ACCESS_TOKEN"` <br>

        {
			"success": true
			"actors": [
				{ "id": 1, "name": "Shahrukh", "gender": "Male", "age": 35 }
			  ],
		}


#### GET /movies

* General: Retrieves movies
* Sample: `curl https://casting-agency19.herokuapp.com/movies -H "Authorization: Bearer ACCESS_TOKEN"`<br>

        {
			"success": true
			"movies": [
				{
					"actors": ["Shahrukh", "Salman"],
					"id": 1,
					"title": "Life",
					"release_date": "Mon, 17 May 2022 00:00:00 GMT"
				}
			  ],
		}

#### POST /actors

* General: Creates new actor
* Sample: `curl https://casting-agency19.herokuapp.com/actors -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{
            "name": "Deepika",
            "age": "29",
            "gender": "Female"
        }'`<br>
		
		{
			"created": 1,
			"success": true
		}


#### POST /movies

* General: Creates new movie
* Sample: `curl https://casting-agency19.herokuapp.com/movies -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{
            "title" : "Titans",
			"release_date" : "10/9/2022"}
        }'`<br>
		
		{
			"created": 1,
			"success": true
		}
		
#### PATCH /actors/\<int:id\>

* General: Creates new actor
* Sample: `curl https://casting-agency19.herokuapp.com/actors/1 -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{
            "name": "Aamir"
        }'`<br>
		
		{
			"success": true
			"actor": { "id": 1, 
					   "name": "Aamir", 
					   "gender": "Male", 
					   "age": 35},
		}
		
#### PATCH /movies/\<int:id\>

* General: Creates new movie
* Sample: `curl https://casting-agency19.herokuapp.com/movies/1 -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{
            "title" : "Titans"
        }'`<br>
		
		{
			"success": true
			"movie": [
				{
					"actors": ["Shahrukh", "Salman"],
					"id": 1,
					"title": "Titans",
					"release_date": "Mon, 17 May 2022 00:00:00 GMT"
				}
			  ],
		}
		
#### DELETE /actors/\<int:id\>

* General:Deletes an actor
* Sample: `curl https://casting-agency19.herokuapp.com/actors/2 -X DELETE -H "Authorization: Bearer ACCESS_TOKEN"`<br>

        { 
            "success": true,
			"delete": 2
        }
		
#### DELETE /movies/\<int:id\>

* General:Deletes a movie
* Sample: `curl https://casting-agency19.herokuapp.com/movies/2 -X DELETE -H "Authorization: Bearer ACCESS_TOKEN"`<br>

        { 
            "success": true,
			"delete": 2
        }
		

Note: All the endponts have been tested on postman, reviewer might use these tokens to test endpoints and access heroku url mentioned above.
