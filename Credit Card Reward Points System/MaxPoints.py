# ● Rule 1: 500 points for every $75 spend at Sport Chek, $25 spend at Tim Hortons and $25 spend at Subway
# ● Rule 2: 300 points for every $75 spend at Sport Chek and $25 spend at Tim Hortons
# ● Rule 3: 200 points for every $75 spend at Sport Chek
# ● Rule 4: 150 points for every $25 spend at Sport Chek, $10 spend at Tim Hortons and $10 spend at Subway
# ● Rule 5: 75 points for every $25 spend at Sport Chek and $10 spend at Tim Hortons
# ● Rule 6: 75 points for every $20 spend at Sport Chek
# ● Rule 7: 1 point for every $1 spend for all other purchases (including leftover amount)

# Method to calculate the total points earned given amount_cents from sports check (sc), tim hortons (th), subway (sw), and general stores (g) respectively
def points_earned(sc, th, sw, g):
    flag = True
    points_earned = 0

    while flag:
        if sc > 0 or th > 0 or sw > 0 or g > 0:
            if sc >= 75 and th >= 25 and sw >= 25:  # ● Rule 1
                sc -= 75  # subtract dollars accounted for in points total
                th -= 25
                sw -= 25
                points_earned += 500  # add points to total
            if sc >= 75 and th >= 25:  # Rule 2
                sc -= 75
                th -= 25
                points_earned += 300
            if sc >= 75:  # Rule 3
                sc -= 75
                points_earned += 200
            if sc >= 25 and th >= 10 and sw >= 10:  # Rule 4
                sc -= 25
                th -= 10
                sw -= 10
                points_earned += 150
            if sc >= 25 and th >= 10:  # Rule 5
                sc -= 25
                th -= 25
                points_earned += 75
            if sc >= 20:  # Rule 6
                sc -= 20
                points_earned += 75
            else:  # Rule 7
                points_earned += max(0, sc) + max(0, th) + max(0, sw) + max(0, g)  # add positive remaining points and/or general store points
                sc -= sc
                th -= th
                sw -= sw
                g -= g
        else:
            flag = False  # end while loop when all remaining points are counted
    return points_earned
