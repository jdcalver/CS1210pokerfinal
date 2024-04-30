if hand == "Full house":
            card1 = 0
            card2 = 0
            totalCard = 0
            if x[0] == y[0]:
                needed = x[0]
                totalCard += 2
                for val in community_cards:
                    if val[0] == x[0] or val[0] == y[0]:
                        totalCard += 1
                if totalCard >= 3:
                    return "You have a full house"
                    odd_control = False
                else:
                    needed = x[0] if totalCard == 2 else y[0]
                    prob = ((3 - totalCard) / 47) * 100
                    return f"The probability of hitting two more {needed}'s " \
                           f"to get a full house is {prob:.2f}%"
                    odd_control = False
            elif x[0] != y[0]:
                card1 += 1
                card2 += 1
                for val in community_cards:
                    if val[0] == x[0]:
                        card1 += 1
                    elif val[0] == y[0]:
                        card2 += 1
                if card1 >= 3 or card2 >= 3:
                    return "You have a full house"
                    odd_control = False
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
            prob = ((3 - totalCard) / 47) * 100
            return f"The probability of hitting two more {needed}'s " \
                   f"to get a full house is {prob:.2f}%"
            odd_control = False
            