#RUSSIAN ROULETTE GAME
import random
import time

slots = [1, 2, 3, 4, 5, 6]
trigger_options = ["ss", "sd"]
bulletpos = 0

def reset_game():
    global slots, bulletpos
    slots = [1, 2, 3, 4, 5, 6]
    bulletpos = store_bullet()
    print("\n🎲 Round has ended — new round starting!\n")
    return

def store_bullet():
    return random.choice(slots)

bulletpos = store_bullet()

def player_shoot_self():
    global slots
    chamber = random.choice(slots)
    if chamber == bulletpos:
        print("💥 You died, you lose.")
        reset_game()
        return True
    else:
        print("Blank, you survived.")
        slots.remove(chamber)
        return False

def player_shoot_dealer():
    global slots
    chamber = random.choice(slots)
    if chamber == bulletpos:
        print("💥 Dealer died, you win.")
        reset_game()
        return True
    else:
        print("Blank, dealer survived.")
        slots.remove(chamber)
        return False

def dealer_shoot_player():
    global slots
    chamber = random.choice(slots)
    if chamber == bulletpos:
        print("💥 Dealer shot you! You lose.")
        reset_game()
        return True
    else:
        print("Blank, you survived.")
        slots.remove(chamber)
        return False

def dealer_shoot_self():
    global slots
    chamber = random.choice(slots)
    if chamber == bulletpos:
        print("💥 Dealer shot themselves, they lose.")
        reset_game()
        return True
    else:
        print("Blank, dealer survived")
        slots.remove(chamber)
        return False

def dealer_random_action():
    action = random.choice(["ds", "dd"])
    if len(slots) == 1:
        return dealer_shoot_player()
    if action == "ds":
        print("Dealer chooses to shoot the player...")
        time.sleep(2)
        return dealer_shoot_player()
    elif action == "dd":
        print("Dealer chooses to shoot themselves...")
        time.sleep(2)
        return dealer_shoot_self()

def game_turn():
    while True:
        # Player's turn
        triggerQ = input("Input 'ss' to shoot self, Input 'sd' to shoot dealer ").lower()
        if triggerQ not in trigger_options:
            print("Invalid input; input 'ss' or 'sd'")
            continue
        if triggerQ == "ss":
            print("Shooting self... ")
            time.sleep(2)
            if player_shoot_self():
                continue
        else:
            print("Shooting dealer... ")
            time.sleep(2)
            if player_shoot_dealer():
                continue
        # Dealer's turn
        time.sleep(2)
        print("\nDealer's turn:")
        if dealer_random_action():
            continue

game_turn()
