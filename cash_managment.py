# Inputs for cash managent strategy:
# Cash amount 
# Space for card counting input
# Martingale strategy at extra input

class FixedPositionSize:

    def __init__(self, position_size):
        self.pos_size = position_size

    def place_wager(self, seen_cards, current_cash, outcomes):
        if current_cash > self.pos_size:
            return self.pos_size
        elif current_cash > 0:
            return current_cash
        else: return 0


class Martingale:

    def __init__(self, base_wager):
        self.base_wager = base_wager

    def place_wager(self, seen_cards, current_cash, outcomes):
        if outcomes[-1] < 0:
            return abs(outcomes[-1]*2)
        else: return self.base_wager

class CardCountingConfidence:

    def __init__(self):
        pass 

class CashManagement:

    def __init__(self):
        pass 

    def place_wager(self, seen_cards, current_cash, outcomes):
        pass



if __name__ == "__main__":
    pass