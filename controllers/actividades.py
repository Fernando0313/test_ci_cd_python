from flask_restful import Resource,reqparse

serializador = reqparse.RequestParser(bundle_errors=True)
serializador.add_argument(
    'actividadNombre',
    required=True,
    location='json',
    help='Falta la actividad nombre',
    type=str
)

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
    
    def post(self):
        data : dict = serializador.parse_args()

        actividadCreada = {
            "actividadId": 50,
            "actividadNombre": data.get('actividadNombre')
        }
        return{
            "message": "actividad creada exitosamente",
            "content": actividadCreada
        }