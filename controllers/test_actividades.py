from app import app
from unittest import TestCase, result

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

    def test_post_actividades(self):
        respuesta = self.app.post('/actividades')

        self.assertEqual(respuesta.status_code,400)
        self.assertDictEqual(respuesta.json, dict(
            message={'actividadNombre': 'Falta la actividadNombre'}
        ))
    
    def test_post_actividades(self):
        respuesta = self.app.post(
            '/actividades', json={
                'actividadNombre': 'Hacer la tarea de  backend'
            }
        )
        self.assertEqual(respuesta.status_code, 201)
        self.assertIsNone(respuesta.json)
        
