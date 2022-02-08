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
        print('How many players are there? (1 for Human vs AI, 2 for Human vs Human?)')
        
        
        next_step = False
        while next_step is False:


            player_count = int(input(''))
                        
            if player_count == 1:  
                next_step is True
                
                self.human_one.human_player()
                print(f'Player 1 is {self.human_one.name}!')
                self.ai_one.ai_player()
                print(f'AI Player is {self.ai_one.name}!')
                next_step = True
                self.human_ai_match()

            elif player_count == 2:
                  
                self.human_one.human_player()
                self.human_two.human_player()
                print(f'Player One is {self.human_one.name}.')
                print(f'Player Two is {self.human_two.name}.')
                next_step = True
                print("You've selected Human vs Human.")
                self.human_human_match()

            elif player_count != 1 or 2:
                    print('Please select the appropriate option.')

            # else:
            #     print('Lets Duel!')
            #     self.ai_one.ai_turn(self) 
                        
    
    
    def human_human_match(self):
        self.human_one.human_choice()
        self.human_two.human_choice()
    
    def human_ai_match(self):
        self.human_one.human_choice()
        player_choice = self.human_one.chosen_gesture
        self.ai_one.ai_turn(player_choice)