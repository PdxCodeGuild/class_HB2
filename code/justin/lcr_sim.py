'''
Justin Young
Optional Lab, "LCR Simulator"
https://github.com/PdxCodeGuild/class_orchid/blob/main/1%20Python/labs/LCR.md
Version1
'''

import random

def dice_roll():
    dice = ['L','R','C','.','.','.']
    x = random.choice(dice)
    return x
players = []
while True:
    player = input("Enter player name or 'done' to finish: ")
    if player.lower() == 'done':
        break
    else:
        players.append({'name': player.lower(), 'chips': 3})
        continue

def game():
    p_t = 0
    pot = 0
    cur_player = players[p_t]
    print(cur_player['name'] + 'is up to roll.')    
    for x in range(cur_player['chips']):
        print(x)
        r = dice_roll()
        print(r)                                    
        if r == 'L':
            b = players[int(p_t) - 1]
            b['chips'] += 1
            print(b)
        elif r == 'R':
            b = players[int(p_t) + 1]
            b['chips'] += 1
            print(b)
        elif r == 'C':
            pot += 1
            print(pot)
  
    # if dice_roll() == 'L':

print(game())
# print(game())
