from flask_restful import Resource


class OpenRiceHome(Resource):
    def get(self):
        return {"results": "Hello!"}
