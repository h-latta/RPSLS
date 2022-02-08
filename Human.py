from os import access
from player import Player

class Human(Player):
    def __init__(self):
        # self.wins = 0
        # self.name = 'Jim'
        # self.chosen_gesture = ''
        super().__init__()
        # self.gestures_list


    def human_player(self):
        user_name = input(f'Please enter in player name... ')
        self.name = user_name

    def human_choice(self):
        accept_input = False
        while accept_input == False:
            print('Enter 0 for Rock')
            print('Enter 1 for Paper')
            print('Enter 2 for Scissors')
            print('Enter 3 for Lizard')
            print('Enter 4 for Spock')
            chosen_gesture = input('Enter your chosen number. ')
            final_number = int(chosen_gesture)
            if final_number > len(self.gestures_list):
                print('Choose a valid option.')
            elif final_number <= len(self.gestures_list):
                accept_input = True
                self.chosen_gesture = self.gestures_list[(final_number)]

 