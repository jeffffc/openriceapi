from static import areas
from flask_restful import Resource


class OpenRiceAreas(Resource):
    def get(self, area_id=None):
        if not area_id:
            d = {"results": areas}
        else:
            if area_id == 1:
                d = {"results": [{"id": 1999, "name": "香港島", "link": "/district/1999"},
                                 {"id": 1008, "name": "西環", "link": "/district/1008"},
                                 {"id": 1001, "name": "上環", "link": "/district/1001"}]}
        return d
