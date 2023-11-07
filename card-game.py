class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    # def getKart(self):
    #     return f"{self.type} {self.value}"
    
    def __repr__(self):
        return f"{self.type} {self.value}"
    
        
clubs5 = Card("Clubs", "5")
diamondsA = Card("Diamonds", "A")

# print(clubs5.getKart())
print(diamondsA)
