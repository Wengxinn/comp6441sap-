"""
Written by WENG XINN CHOW on 07.04.2022
Reverse engineering to find the flag for Time to Eat CTFlearn
"""

EATEATEAT = 3
EATEATEATEAT = 4
EATEATEATEATEAT = 2


def reverse_eat(eat):
    """
    Reverse function EAt to find the two strings - eat, eats, given eAt
    """
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = "E10a23t9090t9ae0140"
    # From original
    # Ate(aTE(aten(eat)))
    # Ate(eat[::-1]) = Eat9 + eat[::-1][:3] = Eat9 + 3 characters
    eats = "Eat9___"

    while eat1 < len(eat) and eat2 < len(eats):
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            # previously modified + current (from eAt) + remaining unknowns
            eats = eats[:eat2] + eAt[eateat] + eats[eat2+1:]
            eat2 += 1
        else:
            # previously modified + current (from eAt) + remaining unknowns
            eat = eat[:eat1] + eAt[eateat] + eat[eat1+1:]
            eat1 += 1
        eateat += 1

    return eat, eats

# From original
# eaT(eat)
# Eating(eat[:3]) + eat[::-1] =  str(int(eat[:3] * 3)) + eat[::-1]
# 2 choices for (eat[:3] * 3): 3 digits or 4 digits
# eat has 9 characters

# 4 digits
eat, eats = reverse_eat("----_________")
# Check eat and eats - eat[4:7] and eats[-3:] are both starts of original eat
if eat[4:7] == eats[-3:]:
    print(str(int(eat[:4]) // 3) + eat[4:len(eat)-4+1][::-1])

# 3 digits 
eat, eats = reverse_eat("---_________")
# Check eat and eats - eat[3:6] and eats[-3:] are both starts of original eat
if eat[3:6] == eats[-3:]:
    print(str(int(eat[:3]) // 3) + eat[3:len(eat)-3+1][::-1])

