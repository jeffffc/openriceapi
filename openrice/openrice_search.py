from .utils import search
from flask_restful import Resource, abort


class OpenRiceSearch(Resource):
    def get(self, searchtext=None):
        if searchtext == "" or not searchtext:
            return abort(404, message="Please enter your query text.")
        else:
            return search(searchtext)
