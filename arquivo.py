from flask import Flask
from flask_restful import Api
from recursos.dados import Jogador, JogadorCaro
app = Flask(__name__)
api = Api(app)

api.add_resource(Jogador,'/jogadores_nba')
api.add_resource(JogadorCaro,'/jogador/<string:nome_jogador>')

if __name__ == "__main__":
    app.run(debug=True)















