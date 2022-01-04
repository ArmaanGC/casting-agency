import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor, db_drop_and_create_all


#Creating headers

cast_assis_header = {
    'Authorization': "Bearer " + os.environ.get('CASTING_ASSISTANT')
}

cast_dir_header = {
    'Authorization': "Bearer " + os.environ.get('CASTING_DIRECTOR')
}

exec_prod_header = {
    'Authorization': "Bearer " + os.environ.get('EXECUTIVE_PRODUCER')
}

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            # self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    #test endpoint: get:actors
    #role: executive producer
    def test_get_actors1(self):
        res = self.client().get('/actors',
                                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #role: casting director
    def test_get_actors2(self):
        res = self.client().get('/actors',
                                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #role: casting assistant
    def test_get_actors3(self):
        res = self.client().get('/actors',
                                headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #test endpoint: get:movies
    #role: executive producer
    def test_get_movies1(self):
        res = self.client().get('/movies',
                                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #role: casting director
    def test_get_movies2(self):
        res = self.client().get('/movies',
                                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #role: casting assistant
    def test_get_movies3(self):
        res = self.client().get('/movies',
                                headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #test endpoint: post:actors
    #role: executive producer

    def test_create_actor(self):
        actor = {'name': 'Shahrukh', 'age': '38',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                headers=exec_prod_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: casting director
    #negative scenario: 422

    def test_create_actor_error_422(self):
        actor = {'name': 'Error',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                headers=cast_assis_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Unprocessable")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_create_actor_casting_assistant(self):
        actor = {'name': 'Aamir', 'age': '40',
                     'gender': 'Male'}
        res = self.client().post('/actors', json=actor,
                headers=cast_assis_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    #test endpoint: post:movies
    #role: executive producer

    def test_create_movies(self):
        movie = {'title': 'Walking_dead',
                     'release_date': '17/6/2021'}
        res = self.client().post('/movies', json=movie,
                headers=exec_prod_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: executive producer
    #negative scenario: 422

    def test_create_movies_error_422(self):
        movie = {'title': 'Life'}
        res = self.client().post('/movies', json=movie,
                headers=exec_prod_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Unprocessable")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_create_movies_casting_assistant(self):
        movie = {'title': 'Life of Pie',
                     'release_date': '17/6/2021'}
        res = self.client().post('/actors', json=movie,
                headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    #test endpoint: delete:actors
    #role: executive producer

    def test_delete_actors(self):
        res = self.client().delete('/actors/1', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    #role: casting director
    #negative scenario: 404

    def test_delete_actors_error_404(self):
        res = self.client().delete('/actors/400', headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Resource Not found")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_delete_actors_casting_assistant(self):
        res = self.client().delete('/actors/1', headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    #test endpoint: delete:movie
    #role: executive producer

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    #role: executive producer
    #negative scenario: 404

    def test_delete_movie_error_404(self):
        res = self.client().delete('/movies/400', headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Resource Not found")

    #role: casting assistant
    #negative scenario: insufficient permissions

    def test_delete_movie_casting_assistant(self):
        res = self.client().delete('/movies/1', headers=cast_assis_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    #test endpoint: update:actors
    #role: executive producer

    def test_update_actor(self):
        actor = {'name': 'Vicky'}
        res = self.client().patch('/actors/2', json=actor,
                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: castig director
    #negative scenario: 400

    def test_update_actor_error_400(self):
        res = self.client().patch('/actors/1', json=None,
                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Bad Request")

    #test endpoint: update:movies
    #role: executive producer

    def test_update_movies(self):
        actor = {'name': 'Vicky'}
        res = self.client().patch('/movies/2', json=actor,
                headers=exec_prod_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #role: castig director
    #negative scenario: 400

    def test_update_movies_error_400(self):
        res = self.client().patch('/movies/1', json=None,
                headers=cast_dir_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            "Error: Bad Request")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
