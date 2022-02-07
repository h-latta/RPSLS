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
        print('How many players are there?')