# imdbsite
api to get details for a movie just like imdb

An api interface to search and find movies by name,directors and genres.

Is uses data from imdb.json

It uses mysql database with below connection details

		'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',


Commands to run for testing api:

Deactivate virtual environment by using command : deactivate

1.) ./manage.py migrate
2.) ./manage.py populate_movies
3.) ./manage.py runserver


api to get all movies details : http://localhost:8000/api/movies

api to get movies filter by movie name : http://localhost:8000/api/movies?name=star

api to get movies filter by movie name and director name : http://localhost:8000/api/movies?name=star&director=George

api to get movies filter by genre name : http://localhost:8000/api/movies?genre=Family
