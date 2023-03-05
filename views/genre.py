from flask_restx import Namespace, Resource

from container import genre_service
from dao.model.genre import genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_movies = genre_service.get_all()
        return genres_schema.dump(all_movies), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if not genre:
            return "Movie not found", 404
        return genre_schema.dump(genre), 200
