import random
import csv

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
    print("The hands you can ask to see the "
          "probabilities of are: "
          "Flush, Three of a kind, Four of a kind, "
          "Straight, Full House, Pair, High Card.")
    hand = input("Enter what hand you want to see the probability for: ")
    if hand == "Flush":
        suit = ""
        prob = 0
        totalCard = 0
        card1 = 0
        card2 = 0
        if x[1] == y[1]:
            suit = x[1]
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
            if card1 <= 2 and card2 <= 2:
                return"A flush is not possible"
            if (card1 > card2):
                suit = x[1]
                totalCard += card1
            elif (card1 < card2):
                suit = y[1]
                totalCard += card2
            elif card1 == card2:
                return "A flush is not possible"
        prob = (13 - totalCard) * 4
        return (f"The probability of hitting another {suit} "
                f"to get a flush is {prob}%")     
    if hand == "Three of a kind":
        needed = ""
        card1 = 0
        card2 = 0
        totalCard = 0
        if x[0] == y[0]:
            needed = x[0]
            totalCard += 2
            for val in community_cards:
                if val[0] == x[0] or val[0] == y[0]:
                    print("You have a three of a kind!")
                elif val[0] != x[0] or val [0] != y[0]:
                    pair_prob = (2/47) * 100
                    return(f"The probability of hitting another {needed} "
                           f"to get a three of a kind is {pair_prob:.2f}%.")
        if x[0] != y[0]:
            card1 += 1
            card2 += 1
            for val in community_cards:
                if val[0] == x[0]:
                    card1 += 1
                elif val[0] == y[0]:
                    card2 += 1
            if card1 >= 3 or card2 >= 3:
                return("You have a three of a kind")
            elif card1 == 0 and card2 == 0:
                for val in community_cards:
                    lst = []
                    lst.append(val[0])
                for i in range(1, len(lst)):
                    if lst[i-1] == lst[i]:
                        totalCard += 1
            else:
                if card1 > card2:
                    needed = x[0]
                    totalCard = card1
                elif card1 < card2:
                    needed = y[0]
                    totalCard = card2
        prob = (totalCard / 47) * 100
        return(f"The probability of hitting another {needed} "
               f"to get a three of a kind is {prob:.2f}%")
    if hand == "Four of a kind":
        needed = ""
        card1 = 0
        card2 = 0
        totalCard = 0
        if x[0] == y[0]:
            totalCard += 2
            for val in community_cards:
                if val[0] == x[0] or val[0] == y[0]:
                    totalCard += 1
                if totalCard > 3:
                    return("You have a four of a kind")
        elif x[0] != y[0]:
            card1 += 1
            card2 += 1
            for val in community_cards:
                if val[0] == x[0]:
                    card1 += 1
                elif val[0] == y[0]:
                    card2 += 1
            if card1 >= 4 or card2 >= 4:
                return("You have a four of a kind")
            elif card1 == 1 and card2 == 1:
                return("Four a kind is not possible")
            elif card1 > card2:
                needed = x[0]
                totalCard = card1
            elif card1 < card2:
                needed = y[0]
                totalCard = card2
        prob = (((4 - totalCard) / 47) * 100) * 0.5
        return (f"The probability of hitting two more {needed}'s "
                f"to get a four of a kind is {prob:.2f}%")
    if hand == "High Card":
        if x[0] == "Jack" and y[0] == "Queen":
            return("You have a Queen, that might be a high card.")
        elif x[0] == "Jack" and y[0] == "King":
            return("You have a King, that might be a high card.")
        elif x[0] == "Jack" and y[0] == "Ace":
            return("You have an Ace, that is definitely a high card.")
        elif x[0] == "Queen" and y[0] == "King":
            return("You have a King, that might be a high card.")
        elif x[0] == "Queen" and y[0] == "Ace":
            return("You have an Ace, that is definitely a high card.")
        elif x[0] == "King" and y[0] == "Ace":
            return("You have an Ace, that is definitely a high card.")
        elif x[0] == "Queen":
            return("You have a Queen, that might be a high card.")
        elif x[0] =="Jack":
            return("You have a Jack, that might be a high card.")
        elif x[0] == "King":
            return("You have a King, that might be a high card.")
        elif x[0] == "Ace":
            return("You have an Ace, that is definitely a high card.")
        elif y[0] == "Jack":
            return("You have a Jack, that might be a high card.")
        elif y[0] == "Queen":
            return("You have a Queen, that might be a high card.")
        elif y[0] == "King":
            return("You have a King, that might be a high card.")
        elif y[0] == "Ace":
            return("You have an Ace, that is definitely a high card.")    
        else:
            return("You don't have a high card, uh oh.")
    if hand  == "Pair":
        needed1 = x[0]
        needed2 = y[0]
        if x[0] == y[0]:
            return("You already have a pair")
        for val in community_cards:
            if val[0] == x[0]:
                return("You already have a pair!")
            elif val[0] == y[0]:
                return("You already have a pair!")
            else:
                prob = (6 / 47) * 100
                return(f"The odds you hit another {needed1} or "
                       f"{needed2} to get a pair is {prob:.2f}%")
                
        
    
                

print(odds(card1, card2))
pot = 0
bet = input("Considering your probabilities, do you want to bet? y/n: ")
if bet == "y":
    amount = int(input("Let's gamble! Enter the amount you wish to raise: "))
    pot += amount
    print(f"OK, assuming this is a two person game "
          f"and the blind is 5 dollars, then the "
          f"pot is {pot + 10:,}$! "
          f"Fingers crossed you win all that money!")
elif bet == "n":
    print("It's always smart to not gamble.")
    
further = input("Do you want to see the probability that your "
                "initial cards will win? y/n: ")
if further == "y":
    with open("pre_flop_odds_chart.csv", newline="") as fh:
        print("To find your cards winning probability, "
              "rewrite using the following syntax:\n"
              "Two Aces = Pair of A's \n"
              "Two Kings = Pair of K's \n"
              "Two Queens = Pair of Q's \n"
              "Two Jacks = Pair of J's \n"
              "Two Tens = Pair of T's \n"
              "Two Nines = Pair of 9's \n"
              "etc for the rest of number card pairs\n"
              "For combinations of cards, not pairs:\n"
              "Nine Ace suited = 9/A suited \n"
              "Eight Ten unsuited = 8/T unsuited \n"
              "Two Four suited = 2/4 suited \n"
              "Make sure to include whether suited or unsuited for non-pairs\n"
              "Also make sure to input the smaller card first\n"
              "Be sure to follow the capitalization rules above as well")
        response = input("Enter your cards following the rules above: ")     
        reader = csv.reader(fh)
        next(reader)
        while True:
            for row in reader:
                if row[0] == response:
                    print(f"With a {card1, card2} in your hand "
                          f"You have a {row[1]} probability of winning! "
                          f"Hopefully that pot of {pot + 10:,}$ is yours!")
                    break
else:
    print("Flying blind! Best of luck.")
        


    
  
    