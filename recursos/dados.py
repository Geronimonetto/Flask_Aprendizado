from flask_restful import Resource


nome_jogadores = [
    {   
        'Jogador':'Lebron James',
        'Média de pontos':'23 pontos',
        'Média de rebotes':'9 rebotes',
        'Média de Assistências':'7.2 assistências'
    },
    {   
        'Jogador':'Stephen curry',
        'Média de pontos':'30 pontos',
        'Média de rebotes':'5.6 rebotes',
        'Média de Assistências':'6.5 assistências'
    },
    {   
        'Jogador':'Jayson Tatum',
        'Média de pontos':'21 pontos',
        'Média de rebotes':'7.4 rebotes',
        'Média de Assistências':'6.3 assistências'
    },
    {   
        'Jogador':'Michael Jordan',
        'Média de pontos':'30.1 pontos',
        'Média de rebotes':'5.3 rebotes',
        'Média de Assistências':'6.2 assistências'
    },


]

class Jogador(Resource):
    def get(self):
        return {'Jogadores NBA':nome_jogadores}
    
