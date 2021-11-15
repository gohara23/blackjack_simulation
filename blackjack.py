import numpy as np
import players
import cash_managment
from dataclasses import dataclass


class BlackjackGame:

    def __init__(self, num_decks=4):
        self.dealer = players.Dealer()
        self.players = []
        self.seen_cards = []
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

    def add_player(self, Player):
        '''
        Adds a player to the list of player

        :type Player: Player object
        '''
        self.players.append(Player)

    def deal_card(self):
        return self.shoe.pop()

    def deal_turn(self):
        '''
        Deals cards to dealer and players.

        Players have knowledge of first dealer card
        
        '''
        card = self.deal_card()
        self.dealer.cards.append(card)
        self.seen_cards.append(card)
        for player in self.players:
            card = self.deal_card()
            player.cards.append(card)
            self.seen_cards.append(card)

        self.dealer.cards.append(self.deal_card())

        for player in self.players:
            card = self.deal_card()
            player.cards.append(card)
            self.seen_cards.append(card)
            player.add_dealer_card(self.dealer.cards[0])

    def collect_wagers(self):
        for player in self.players:
            player.place_wager(self.seen_cards)
        


@dataclass
class Card:
    number: int
    suit: str


if __name__ == "__main__":
    game = BlackjackGame()
    game.create_shoe()
    # player = players.Player(strategy, cash_managment.Martingale(25))
    print(game.shoe.pop())


    
