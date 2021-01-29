from random import shuffle
class Card():
    def __init__(self,suit,card):
        self.suit= suit
        self.card= card
    def __repr__(self):
        return f"{self.suit} {self.card}"

class Deck():
    suits=["hearts","clubs","spades","diamonds"]
    cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.card_list=[Card(suit,card) for suit in Deck.suits for card in Deck.cards]
    def number_of_cards(self):
        return len(self.card_list)
    def shuffle_deck(self):
        if(self.number_of_cards()==52):
            shuffle(self.card_list)
    def deal_the_cards(self,number):
        number = min([self.number_of_cards(),number])
        if number==0:
            return "there isn't any card left"
        else:
            result=self.card_list[-number:]
            self.card_list=self.card_list[:-number]
            return result

deck = Deck()
deck.shuffle_deck()
print(deck.number_of_cards())
print(deck.deal_the_cards(12))
print(deck.deal_the_cards(12))
print(deck.deal_the_cards(12))
print(deck.deal_the_cards(12))
print(deck.deal_the_cards(12))
print(deck.deal_the_cards(12))
