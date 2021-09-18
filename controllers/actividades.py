from flask_restful import Resource,reqparse

class ActividadesController(Resource):
    def get(self):
        return{
            "message":None,
            "content":[{
                "actividadId":1,
                "actividadNombre":"Ir a la playa"
            },
            {
                "actividadId":2,
                "actividadNombre":"Ir a la playa"
            },
            {
                "actividadId":3,
                "actividadNombre":"Ir a la playa"
            }]
        },201