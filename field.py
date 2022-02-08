
from human import Human
from ai import Ai

class Field:

    def __init__(self):
        self.human_one = Human()
        self.ai_one = Ai()
        self.human_two = Human()
        self.rounds = 0

    def number_of_players(self):
        print()
        print('*******Welcome to Rock-Paper-Scissors-Lizard-Spock!*******')
        print()
        print('Each match will be Best of 3!')       
        print()
        print('Here is a set rules:')
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
        print()
        print('How many players are there? (1 for Human vs AI, 2 for Human vs Human?)')
        
        next_step = False
        while next_step is False:
            player_count = int(input(''))

            if player_count == 1:  
                print("You've selected Human vs AI.")
                next_step is True
                self.human_one.human_player()
                print()
                print(f'Player 1 is {self.human_one.name}!')
                self.ai_one.ai_player()
                print(f'AI Player is {self.ai_one.name}!')
                print()
                next_step = True
                self.human_ai_match()
                
            elif player_count == 2:
                print("You've selected Human vs Human.")
                self.human_one.human_player()
                self.human_two.human_player()
                print()
                print(f'Player One is {self.human_one.name}.')
                print(f'Player Two is {self.human_two.name}.')
                print()
                next_step = True
                self.human_human_match()
            
            elif player_count != 1 or 2:
                    print('Please select the appropriate option.')
    
    def human_human_match(self):
        win = False
        while self.human_one.wins < 2 or self.human_two.wins < 2:
            self.human_one.human_choice()
            self.human_two.human_choice()
            print()
            print(f'{self.human_one.name} chose {self.human_one.chosen_gesture}')
            print(f'{self.human_two.name} chose {self.human_two.chosen_gesture}')
            print()
            self.gestures(self.human_one, self.human_two)
            print(f'{self.human_one.name} has won {self.human_one.wins}. {self.human_two.name} has won {self.human_two.wins}. End of Round {self.rounds}.')
            print()
            if self.human_one.wins == 2:
                win = True
                print(f'{self.human_one.name} won the game!')
                break
            
            elif self.human_two.wins == 2:
                win = True
                print(f'{self.human_two.name} won the game!')
                break
    
    def human_ai_match(self):
        
        rounds = self.ai_one.rounds
        win = False
        while self.human_one.wins < 2 or self.ai_one.wins < 2:
            self.human_one.human_choice()
            self.ai_one.ai_turn()
            print()
            print(f'{self.human_one.name} chose {self.human_one.chosen_gesture}')
            print(f'{self.ai_one.name} chose {self.ai_one.chosen_gesture}')
            print()
            self.gestures(self.human_one, self.ai_one)
            self.rounds += 1
            print(f'{self.human_one.name} has {self.human_one.wins} wins. {self.ai_one.name} has {self.ai_one.wins} wins. End of Round {self.rounds}.')
            print()
            if self.human_one.wins == 2:
                win = True
                print(f'{self.human_one.name} won the game!')
                break
           
            elif self.ai_one.wins == 2:
                win = True
                print(f'{self.ai_one.name} won the game!')
                break

    def gestures(self, player_one, player_two):
        count = 0
        #Rock beats Scissors and Lizard
        #Paper beats Spock and Rock
        #Scissors beats Lizard and Paper
        #Lizard beats Paper and Spock
        #Spock beats Scissors and Rock
        if player_one.chosen_gesture == player_two.chosen_gesture:
            print("It's a tie.")
        
        elif player_one.chosen_gesture == 'Rock':
            
            if player_two.chosen_gesture == 'Scissors' or player_two.chosen_gesture == 'Lizard':
                print('Player One wins!')
                player_one.wins += 1
            
            else:
                print('Player Two wins!')
                player_two.wins += 1
        
        elif player_one.chosen_gesture == 'Paper':
            
            if player_two.chosen_gesture == 'Spock' or player_two.chosen_gesture == 'Rock':
                print('Player One wins!')
                player_one.wins += 1
            
            else:
                print('Player Two wins!')
                player_two.wins += 1
       
        elif player_one.chosen_gesture == 'Scissors':
            if player_two.chosen_gesture == 'Lizard' or player_two.chosen_gesture == 'Paper':
                print('Player One wins!')
                player_one.wins += 1
            else:
                print('Player Two wins!')
                player_two.wins += 1
        elif player_one.chosen_gesture == 'Lizard':
            if player_two.chosen_gesture == 'Paper' or player_two.chosen_gesture == 'Spock':
                print('Player One wins!')
                player_one.wins += 1
            else:
                print('Player Two wins!')
                player_two.wins += 1
        elif player_one.chosen_gesture == 'Spock':
            if player_two.chosen_gesture == 'Scissors' or player_two.chosen_gesture == 'Rock':
                print('Player One wins!')
                player_one.wins += 1
            else:
                print('Player Two wins!')
                player_two.wins += 1
        else:
            print('Player Two wins!')
            player_two.wins += 1


    
