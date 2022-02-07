from human import Human
from ai import Ai

class Field:

    def __init__(self):
        self.human_one = Human()
        self.ai_one = Ai()
        self.human_two = Human()

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
        player_count = int(input())
        next_step = False
        while next_step == False:
            if player_count == 1:
                next_step == True
                print("You've selected Human vs AI.")
                self.human_one.human_player()
                self.ai_one.ai_player()
                print(self.human_one.name)
                print(self.ai_one.name)

            elif player_count == 2:
                next_step == True
                print("You've selected Human vs Human.")
                self.human_one.human_player()
                self.human_two.human_player()
                print(self.human_one.name)
                print(self.human_two.name)
        
            elif player_count != 1 or 2:
                print('Please select the appropriate option.')
                break

    def ai_match(self):
        pass
    
    def human_match(self):
        pass