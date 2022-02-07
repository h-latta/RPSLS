from player import Player

class Human(Player):
    def __init__(self):
        self.name = 'Jim'
        self.chosen_gesture = ''
        super().__init__()
        self.gestures_list


    def human_player(self):
        user_name = input(f'Please enter in player one name...')
        self.name = user_name

    def human_choice(self):
        pass