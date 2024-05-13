#project4
#snack and ladder game
import random
def roll_dice():                                        
    return random.randint(1, 6)

def move_player(player, steps):
    player += steps                                     
    if player > 100:
        player = 100
    return player

def check_snakes_and_ladders(player):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}             
    
    if player in snakes:
        print(f"Oops! You got bitten by a snake! Go back to square {snakes[player]}")
        player = snakes[player]
    elif player in ladders:
        print(f"Yay! You found a ladder! Advance to square {ladders[player]}")
        player = ladders[player]
    return player

def play_snakes_and_ladders():
    player1 = 0
    player2 = 0
    while True:
        input("Player 1, press Enter to roll the dice")
        dice_roll = roll_dice()
        print(f"Player 1 rolled a {dice_roll}")
        player1 = move_player(player1, dice_roll)
        player1 = check_snakes_and_ladders(player1)
        print(f"Player 1 is now on square {player1}")
        if player1 == 100:
            print("Player 1 wins!")
            break
        
        input("Player 2, press Enter to roll the dice")
        dice_roll = roll_dice()
        print(f"Player 2 rolled a {dice_roll}")
        player2 = move_player(player2, dice_roll)
        player2 = check_snakes_and_ladders(player2)
        print(f"Player 2 is now on square {player2}")
        if player2 == 100:
            print("Player 2 wins!")
            break

play_snakes_and_ladders()
