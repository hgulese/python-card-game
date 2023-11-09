from random import shuffle

class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    # def getKart(self):
    #     return f"{self.type} {self.value}"
    
    def __repr__(self):
        return f"{self.type} {self.value}"
    
        
# clubs5 = Card("Clubs", "5")
# diamondsA = Card("Diamonds", "A")

# print(clubs5.getKart())
# print(diamondsA)

class Deck:
    types = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = [Card(type, value) for type in Deck.types for value in Deck.values]
        
        # for type in types:
        #     for value in values:
        #         self.cards.append(Card(type, value))
        
    def numberofCard(self):
        return len(self.cards)
    
    def shuffletheCards(self):
        if self.numberofCard() < 52:
            raise ValueError("you can shuffle the cards without destroying the deck.")
        shuffle(self.cards)
        
    def dealtheCards(self, piece):
        numberofCard = self.numberofCard()
        if numberofCard == 0:
            raise ValueError("no cards")
        piece = min([numberofCard, piece])
        
        cards = self.cards[-piece:]
        self.cards = self.cards[:-piece]
        return cards

deck1 = Deck()
deck1.shuffletheCards()
result = deck1.cards

print(deck1.dealtheCards(7))
print(deck1.numberofCard())

print(result)