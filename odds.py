import random
#on flop multiply oouts by 4, on turn by 2

suits = ["spade", "heart", "diamond", "club"]
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(val, suit) for val in vals for suit in suits]


card1 = random.choice(deck)
card2 = random.choice(deck)
community_cards = ((random.choice(deck)), (random.choice(deck)), (random.choice(deck))) 



print(f"Your cards are {card1, card2}")
if card1[0] == card2[0]:
    print("You have a pair so far.")
if card1[1] == card2[1]:
    print("Your cards are suited.")
print(f"The flop is {community_cards}")
    
def odds(x, y):
    hand = input("enter what hand you want to see the probability for: ")
    if hand == "Flush":
        suit = ""
        prob = 0
        totalCard = 0
        card1 = 0
        card2 = 0
        if x[1] == y[1]:
            totalCard += 2
            for val in community_cards:
               if val[1] == x[1] or val[1] == y[1]:
                   totalCard += 1
            if totalCard < 3:
                return "A flush is not possible"
        elif x[1] != y[1]:
            card1 +=1
            card2 += 1
            for val in community_cards:
                if val[1] == x[1]:
                    card1 +=1
                elif val[1] == y[1]:
                    card2 += 1
            if (card1 > card2):
                suit = x[1]
                totalCard += card1
            elif (card1 < card2):
                suit = y[1]
                totalCard += card2
            elif card1 == card2:
                return "A flush is not possible"
        prob = (13 - totalCard) * 4
        return (f"the probability of hitting another {suit} is {prob}%")
    if hand == "Two Pair":
        needed = ""
        totalCard = 0
        card1 = 0
        card2 = 0
        if x[0] == y[0]:
            needed = x[0]
            totalCard += 2
            for val in community_cards:
                if val[0] == x[0]:
                    totalCard += 1
        elif x[0] != y[0]:
            for val in community_cards:
                if val[0] == x[0]:
                    card1 += 1
                elif val[0] == y[0]:
                    card2 += 1
            if card1 > card2:
                needed = x[0]
                totalCard = card1
            elif card1 < card2:
                needed = y[0]
                totalCard = card2
            #elif totalCard < 2:
                #print("A two pair is not possible")
        prob = ((47 - totalCard) * 4) / 100
        return(f"The probability of hitting another {needed} is {prob}%")
        
            
            
            
    

print(odds(card1, card2))
    
  
    