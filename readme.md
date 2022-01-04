# Casting Agency Project

This project is about company that is responsible for creating movies and managing and assigning actors to those movies.

Following roles and functionalities have been implemented as part of this project:

1. Casting assistant: who can view actors and movies and has limited access.
2. Casting director: who can view and edit actors and movies, also create and delete actors, has limited access to movies.
3. Executive producer: who has all the accesses to view, edit, create and delete actors and movies.

## Motivation

This project helps gain better understanding of all the concepts learned throughout the course and allowed me to implement the knowledge I gathered.

## Setting up project locally

### Dependencies
Developers should have Python3, git, postgres, pip, flask, node, and npm installed.

### Set up environment and install requirements

Setup a virtual environment as this keeps your dependencies for each project separate and organized. Then run below commands to setup environment variables and install requirements.

```bash
python -m venv myvenv
source myvenv/Scripts/activate
source setup.sh
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

## Host the project on heroku

After testing app on loacal, make sure following files are present in source flder:

* app.py
* models.py
* manage.py     
* requirements.txt 
* Procfile        
* runtime.txt
*setup.sh

Following packages are needed for databse migration, make sure they are installed:

* pip install Flask-Script==2.0.6
* pip install Flask-Migrate==2.7.0
* pip install psycopg2-binary==2.9.1

### Deploying to heroku

Install heroku CLI.
Make sure you have an account on heroku as email and password will be prompted while logging from CLI, then follow the steps:

1. Move to project directory as:

```bash
cd project
```

2. Login to heroku as:

```bash
heroku login -i
```

3. Initialize git repo as:

```bash
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

4. Create app on heroku and can be viewed as:

```bash
heroku create [my-app-name] --buildpack heroku/python
git remote -v
```

5. Add postgreSQL addon for your database

```bash
heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]
```

6. App configurations as:

```bash
heroku config --app [my-app-name]
```

Also, you will have to go to the Heroku dashboard >> Particular App >> Settings >> Reveal Config Vars section and save the EXCITED variable and its value as true

7. Add git commits and push:

```bash
git status
git add .
git commit -m "First Commit"
git push heroku master
```

8. Once app is deployed, run migrations:

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
heroku run python manage.py db upgrade --app [my-app-name]
```

9. You app will be live 

## Auth0 details:

1. Domain - dev-jdd6v-si.us.auth0.com
	
2. Client Id - z9n4IAz9fX4I0QYcKdgIzAvuZhJhW1ty

## Heroku deployment

Project is hosted via heroku, link: https://casting-agency19.herokuapp.com/

## Access tokens

* Casting assistant access token:
	
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwYzBlMDljODMwMDZmMWIyMjQ2IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjY1MCwiZXhwIjoxNjQxMzEzODUwLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.OdaUtM4Hbn6_TEUlh7TgPWGQtO-V9OOPdzrg2HNrcF08Q_w8r9Nz4M1GuuBPNMuGqf3bF8_LG8fXaKRrO9VZhD3pHs3kXI7-K8FPv6zsZbj7ZcvfbloNWYlm2WWiFlpQ-wZMrgw0myLom4P3cvxGntwVU5wWdr5oA9HXGvcgdSF4JA6wX_OWJqQhYHZV__Xc1ZUjV1o8aYxPfFa2p_0MJhgILpogcPurewTClYcOyk_49tsnbv4YGLkyH2ovuCyB3Lmj9oHlgN32OCXHX1DIjwIEffp3GYIiL9h-TMYMEvoO9HwhxWCwEK9A3QP6alTv8dGqtAJUQqmYzmFwycnJkA

	
* Casting director access token:
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwOTRmYTJjZDEwMDY5ZWU2Mjc5IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjY0MywiZXhwIjoxNjQxMzEzODQzLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.uIBsOzRMv0a3DrEBkNssHk0uZ1QZNzwIyDDUGYxZ-hNlOswcx09VlyABQxsj4aao6kfZBnHCZrQpqGiygPH3l0knbP-Bu2DqEGZN76bSb9z7De35iMv5JI7NuAgUEgd3SaSTI7J-QLlMg9OAOC0gqZc4NkVGx91OtA_c1SlWN7EYY6kLiNtOEPZXFR5C3U8hWIrVum3xcZU5_WVBM5IjwswuodWChIgE2C-1B1eXzMWmRfISnnmwx7hTJAWNqQ1lrvH0ewycMxE6A3VsUntgFCKXWN1OuedJ-EVy1hICSjOAClyUuWrJjqVwTLoyrVwYx8xBI_IVjfIhXxfPEsBHSw
	
* Executive producer access token:
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwNWZmYTJjZDEwMDY5ZWU2MjZlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjYzOCwiZXhwIjoxNjQxMzEzODM4LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.PMPj3xR9N_XiQ4udbRdxSLIljrsgvPWvhvGIbxLXmqSTqwpmFKEw5lbVtIieVmMFq37jN38-HOfRsGV9LVcsI2_SLGJZqCo7xrA451EkdUK2cXJ-a2BxUGQCo7VMsZSmK0dGR6JL_mT1YUjyGj1TOLW-64zPsGj-TXD9OEn1gpWE62K1rTnX4DImdv02t8IVBV8OUrtYdIcvVVqiTKxzFl_IqS60D2MFEgLvqBjJr-gKURCrziEm-HTNLDIbtCdgnotFrKD7X2ZDgFrC2_YVQ-BGe5HUyG7_1X5y0n8B-hcovT8Zj-CydluLapUOeFa3DMKswk86ZAICSSuUnW0BCQ

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
