from flask_restx import Namespace, Resource

from container import director_service
from dao.model.director import directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_movies = director_service.get_all()
        return directors_schema.dump(all_movies), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        if not director:
            return "Movie not found", 404
        return director_schema.dump(director), 200
