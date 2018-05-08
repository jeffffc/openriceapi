from static import districts
from flask_restful import Resource


class OpenRiceDistricts(Resource):
    def get(self, district_id=None):
        if not district_id:
            d = {"results": districts}
        else:
            if district_id == 1:
                d = {"results": [{"id": 1999, "name": "香港島", "link": "/district/1999"},
                                 {"id": 1008, "name": "西環", "link": "/district/1008"},
                                 {"id": 1001, "name": "上環", "link": "/district/1001"}]}
        return d
