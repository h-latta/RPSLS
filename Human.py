from player import Player

class Human(Player):
    def __init__(self):
        self.name = self.human_player()
        self.chosen_gesture = ''
        super().__init__()
        self.gestures_list


    def human_player(self):
        print('Jim')

    def human_choice(self):
        pass