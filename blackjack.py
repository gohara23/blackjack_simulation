import numpy as np
from dataclasses import dataclass


class BlackjackGame:

    def __init__(self, num_decks=4):
        self.create_shoe(num_decks)

    def create_shoe(self, num_decks=4):
        '''
        Creates objects for the deck

        :param num_decks: number of decks to be included
        :type num_decks: int 

        '''
        # suit does not matter but included for visualization

        suits = ['C', 'S', 'D', 'H']

        self.shoe = []

        for _ in range(num_decks):
            for suit in suits:
                [self.shoe.append(Card(i, suit)) for i in range(1,14)]
   
        np.random.shuffle(self.shoe)


@dataclass
class Card:
    value: int
    suit: str


if __name__ == "__main__":
    game = BlackjackGame()
    game.create_shoe()
    print(game.shoe.pop())


    
