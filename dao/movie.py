# CRUD
from flask import request

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        all_movies = self.session.query(Movie)
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        if director_id is not None:
            all_movies = all_movies.filter(Movie.director_id == director_id)
        if genre_id is not None:
            all_movies = all_movies.filter(Movie.genre_id == genre_id)
        return all_movies

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
