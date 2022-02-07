from human import Human
from ai import Ai

class Field:

    def __init__(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print()
        print('Each match will be Best of 3!')       
        print()
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('Rock crushes Scissors')

    def number_of_players(self):
        print('How many players are there? (1 for Human vs AI, 2 for Human vs Human)')
        player_count = input(int())
        if player_count == 1:
            human_one = Human()
            ai_one = Ai()
        elif player_count == 2:
            human_one = Human()
            human_two = Human()