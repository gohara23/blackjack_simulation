from dataclasses import dataclass
import numpy as np 


# Possible Decisions: Hit, Stand, Double Down
# Dealer must hit up to 17
# May split doubles
# Base Decision on hand and dealer up card

class Dealer:

    def __init__(self):
        self.cards = []

class Player:

    def __init__(self, strategy, cash_management, initial_amount=1000):
        self.cash = initial_amount
        self.strategy = strategy
        self.cash_management = cash_management
        self.cards = []
        self.wagers = []
        self.outcomes = []
        self.cash_history = [initial_amount]
    
    def add_dealer_card(self, dealer_card):
        self.dealer_card = dealer_card

    def place_wager(self, seen_cards):
        wager = self.cash_management.place_wager(seen_cards, self.cash, self.outcomes)
        self.wagers.append(wager)

    def hit(self):
        pass

    def stand(self):
        pass

    def split(self):
        pass 

    def double_down(self):
        pass






if __name__ == "__main__":
    pass