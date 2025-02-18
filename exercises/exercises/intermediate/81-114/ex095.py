# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


data_players = []

class SoccerPlayer:
    name = ''
    goals = 0
    matches = 0
    def __init__(self, name, goals, matches):
        self.name = name
        self.goals = goals
        self.matches = matches
        self.total_goals = sum(goals)

    def to_string(self):
        return f"Player: {self.name} Total of Goals {self.total_goals} Matches {self.matches}"

while True:
    goals = []
    name = (str(input('Player Name: ')))
    matches = (int(input('How many matches: ')))
    for match in range(matches):
        goals.append(int(input(f'How many goals on match {match+1}: ')))
        
    player = SoccerPlayer(name, goals, matches)
    data_players.append(player)

    print(player.to_string())

    add_more = input('Do you want to add another player? (yes/no): ').lower()    
    if add_more != 'yes':
        break

for player in data_players:
    print(player.to_string())