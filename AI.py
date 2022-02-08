from player import Player
import random


class Ai(Player):

    def __init__(self):
        self.wins = 0
        self.name = 'Sheldon'
        self.chosen_gesture = ''
        super().__init__()
        self.gestures_list


    def ai_player(self):
         self.name = 'Sheldon'

    def ai_turn(self):
        self.random_choice = random.choice(self.gestures_list)
        self.chosen_gesture = self.random_choice
        
        # playing_rock = 'Rock'

        # while player_choice == 'Rock':

        #     playing_rock is True
            
        #     if player_choice == self.random_choice:
        #         print('Round Draw')

        #         if self.random_choice == 'Scissors' or 'Lizard':
        #             print('Rock Wins!')

   
