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
        self.gestures(self.human_one, self.human_two)
    
    def human_ai_match(self):
        self.human_one.human_choice()
        self.ai_one.ai_turn()
        self.gestures(self.human_one, self.ai_one)

    def gestures(self, player_one, player_two):
        count = 0
        #Rock beats Scissors and Lizard
        #Paper beats Spock and Rock
        #Scissors beats Lizard and Paper
        #Lizard beats Paper and Spock
        #Spock beats Scissors and Rock
        if player_one.chosen_gesture == 'Rock':
            if player_two.chosen_gesture == 'Scissors' or player_two.chosen_gesture == 'Lizard':
                count += 1
        elif player_one.chosen_gesture == 'Paper':
            if player_two.chosen_gesture == 'Spock' or player_two.chosen_gesture == 'Rock':
                count += 1
        elif player_one.chosen_gesture == 'Scissors':
            if player_two.chosen_gesture == 'Lizard' or player_two.chosen_gesture == 'Paper':
                count += 1
        elif player_one.chosen_gesture == 'Lizard':
            if player_two.chosen_gesture == 'Paper' or player_two.chosen_gesture == 'Spock':
                count += 1
        elif player_one.chosen_gesture == 'Spock':
            if player_two.chosen_gesture == 'Scissors' or player_two.chosen_gesture == 'Rock':
                count += 1
        else:
            print("It's a tie.")
