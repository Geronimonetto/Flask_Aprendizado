from flask import Flask
from flask_restful import Api
from recursos.dados import Jogador
app = Flask(__name__)
api = Api(app)

api.add_resource(Jogador,'/Jogadores_NBA')


if __name__ == "__main__":
    app.run(debug=True)















