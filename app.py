from flask import Flask
from flask_restful import Api
from controllers.actividades import ActividadesController

app = Flask(__name__)
api = Api(app)

api.add_resource(ActividadesController,'/actividades')
print('yo soy un cambio')
print('aea')

if __name__ == '__main__':
    app.run(debug=True)