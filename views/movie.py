from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from dao.model.movie import movies_schema, movie_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "Movie created", 201


# ----------MovieViews--------------
@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if not movie:
            return "Movie not found", 404
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return "", 204

    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
