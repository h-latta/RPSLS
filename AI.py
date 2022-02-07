from player import Player
import random


class Ai(Player):

    def __init__(self):
        self.name = ''
        self.ai_choice = ''
        super().__init__()
        self.gestures_list

    def ai_turn(self, human_choice):
        random_choice = random.choice(self.gestures_list)

    def ai_player(self):
        self.name = 'Sheldon'
