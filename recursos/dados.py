from flask_restful import Resource, reqparse


nome_jogadores = [
    {   
        'Jogador':'Lebron James',
        'Média de pontos':'23 pontos',
        'Média de rebotes':'9 rebotes',
        'Média de assistências':'7.2 assistências'
    },
    {   
        'Jogador':'Stephen curry',
        'Média de pontos':'30 pontos',
        'Média de rebotes':'5.6 rebotes',
        'Média de assistências':'6.5 assistências'
    },
    {   
        'Jogador':'Jayson Tatum',
        'Média de pontos':'21 pontos',
        'Média de rebotes':'7.4 rebotes',
        'Média de assistências':'6.3 assistências'
    },
    {   
        'Jogador':'Michael Jordan',
        'Média de pontos':'30.1 pontos',
        'Média de rebotes':'5.3 rebotes',
        'Média de assistências':'6.2 assistências'
    },


]

class Jogador(Resource):
    def get(self):
        return {'Jogadores NBA':nome_jogadores}
    
class JogadorCaro(Resource):
    def get(self,nome_jogador):
         for nome in nome_jogadores:
            if nome_jogador in nome['Jogador'].capitalize(): 
                return nome
            elif nome_jogador in nome['Jogador'].lower(): 
                return nome
            elif nome_jogador in nome['Jogador'].upper():
                 return nome
         return {'message':"Jogador não encontrado."},404
    def post(self,nome_jogador):
        adicionar_jogador = reqparse.RequestParser()
        adicionar_jogador.add_argument('Jogador')
        adicionar_jogador.add_argument('Média de pontos')
        adicionar_jogador.add_argument('Média de rebotes')
        adicionar_jogador.add_argument('Média de assistências')

        dados_jogadores = adicionar_jogador.parse_args()

        novo_jogador = {
            'Jogador':nome_jogador,
            'Média de pontos':dados_jogadores['Média de pontos'],
            'Média de rebotes':dados_jogadores['Média de rebotes'],
            'Média de assistências':dados_jogadores['Média de assistências']

        }
        nome_jogadores.append(novo_jogador)
        return novo_jogador,200

