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
        print('Enter 0 for Rock')
        print('Enter 1 for Paper')
        print('Enter 2 for Scissors')
        print('Enter 3 for Lizard')
        print('Enter 4 for Spock')
        chosen_gesture = input('Enter your chosen number. ')
        self.chosen_gesture = self.gestures_list[(int(chosen_gesture))]

 