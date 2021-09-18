from app import app
from unittest import TestCase

class TestActividadesController(TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_get_actividades(self):
        respuesta = self.app.get('/actividades')
     
        self.assertEqual(respuesta.json, dict(message=None, content=[{
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
            }]))

        self.assertEqual(respuesta.status_code,201)