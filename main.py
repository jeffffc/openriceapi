from flask_restful import Api
from flask import Flask
from openrice import OpenRiceAreas, OpenRiceSearch, OpenRiceDistricts, OpenRiceHome
import os


app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(OpenRiceSearch, '/search', '/search/<string:searchtext>', endpoint='search')
api.add_resource(OpenRiceAreas, '/area', '/area/<int:area_id>', endpoint='area')
api.add_resource(OpenRiceDistricts, '/district', '/district/<int:district_id>', endpoint='district')
api.add_resource(OpenRiceHome, '/')


if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    debug = os.environ.get('DEBUG', False)
    app.run(debug=debug)
