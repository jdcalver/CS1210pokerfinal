import random


suits = ["spade", "heart", "diamond", "club"]
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(val, suit) for val in vals for suit in suits]


card1 = random.choice(deck)
card2 = random.choice(deck)
flop = ((random.choice(deck)), (random.choice(deck)), (random.choice(deck))) 



print(f"Your cards are {card1, card2}")
if card1[0] == card2[0]:
    print("You have a pair so far.")
if card1[1] == card2[1]:
    print("Your cards are suited.")
print(f"The flop is {flop}")
    
def odds(x, y):
    hand = input("enter what hand you want to see the probability for: ")
    if hand == "Flush":
    if hand == "Straight":
    if hand == "Three of a kind":
    if hand == "Two Pair":
    if hand == "Full House":
    if hand == 
    

print(odds(card1, card2))
    
  
    