import random

class Card:
    __suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    __values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    __figures = list(__values.keys())

    def __init__(self, suit: int, value: int):
        self.suit = Card.__suits[suit]
        self.figure = Card.__figures[value] 
        self.value = Card.__values[self.figure]

    def __str__(self) -> str:
        return f'{self.figure} of {self.suit}'
    
    def __repr__(self) -> str:
        return f'{self.figure} of {self.suit}'
    
class Deck:
    
    def __init__(self) -> None:
        self.cards: list[Card] = []
        for suit in range(4):
            for value in range(13):
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def distribute(self, players: int) -> list[list[Card]]:
        quantity = len(self.cards) // players
        
        self.shuffle()

        decks: list[list[Card]] = [[] * players]

        for _ in range(quantity):
            for player in range(players):
                decks[player].append(self.cards.pop())

        return decks
    
    def __str__(self) -> str:
        string = ''

        for card in self.cards:
            string += card.__str__() + '\n'

        return string

class Player:
    
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards

    def play(self) -> Card:
        return self.cards.pop(0)
    
    def receive(self, cards: list[Card]) -> None:
        for card in cards:
          self.cards.append(card)
            
class Game:
    
    def __init__(self, players: list[Player], deck: Deck):
        self.players = players
        self.deck = deck
        self.round_cards: list[Card] = []

    def next_round(self) -> Player | list[Player]:
        win = self.check_win()
        if len(win) == 1:
            return win[0]

        self.round_cards.append(self.players[0].play())
        self.round_cards.append(self.players[1].play())

        if (self.round_cards[0].value > self.round_cards[1].value):
            self.players[0].receive(self.round_cards)
            return self.players[0]
        
        elif (self.round_cards[1].value > self.round_cards[0].value):
            self.players[1].receive(self.round_cards)
            return self.players[1]
        
        return self.players
    
    def check_win(self) -> list[Player]:
        winners = []

        for player in self.players:
            if len(player.cards):
                winners.append(player)

        return winners
        
if __name__ == '__main__':
    deck = Deck()
    hands = deck.distribute(2)
    players = [Player('Arthur', hands.pop()), Player('Bruna', hands.pop())]