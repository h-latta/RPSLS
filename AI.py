from player import Player
import random


class Ai(Player):

    def __init__(self):
        self.wins = 0
        self.name = 'Sheldon'
        self.ai_choice = ''
        super().__init__()
        self.gestures_list


    # def ai_player(self):
    #     self.name = 'Sheldon'

    def ai_turn(self, player_choice):
        self.random_choice = random.choice(self.gestures_list)
        
        playing_rock = 'Rock'

        while player_choice == 'Rock':

            playing_rock is True
            
            if player_choice == self.random_choice:
                print('Round Draw')

                if self.random_choice == 'Scissors' or 'Lizard':
                    print('Rock Wins!')

   
