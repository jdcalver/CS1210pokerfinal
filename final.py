"""
Patrick Aber
Final
"""
import csv
import random
import math



print("The syntax is as follows: \n"
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

    
with open ("pre_flop_odds_chart.csv", newline="") as fh:
    reader = csv.reader(fh)
    next(reader)
    while True:
        chosen_hand = input("Enter your cards following the above syntax: ")
        for row in reader:
            if row[0] == chosen_hand:
                print(f"You have a {row[1]} probability of winning!")
        break 
       
        
    
        
            
                
       
            
                       
        
        
        
            
        
              












        
        
        
        
