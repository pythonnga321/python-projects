import random
import time

loserolls = [1, 2, 3]
winrolls = [4, 5, 6]
opp_choice = [1, 2]
hitmiss = [1, 2]

def gun():
    bullets = random.randint(1, 8)
    while bullets > 0:
        time.sleep(0.3)
        bullets -= 1
        print("💥POP💥")

def choose_banker():
    return random.choice([1, 2])

def roll_dice(player_name):
    dice1 = random.randint(1, 6)
    print(f"🎲 {player_name} rolled Dice 1: {dice1}")
    time.sleep(1)

    dice2 = random.randint(1, 6)
    print(f"🎲 {player_name} rolled Dice 2: {dice2}")
    time.sleep(1)

    dice3 = random.randint(1, 6)
    print(f"🎲 {player_name} rolled Dice 3: {dice3}")
    time.sleep(1)

    return sorted([dice1, dice2, dice3])

def check_for_doubles(dices):
    return len(set(dices)) < 3

def start_game():
    banker = choose_banker()

    if banker == 1:
        print("🏦 You are the banker. 🏦")
        try:
            bet = int(input("💰 Choose a bet amount: "))
        except ValueError:
            print("❌ You must enter a number. Setting bet to $100.")
            bet = 100
        while bet > 1000:
            bet = int(input("⚠️ Max is $1000. Choose again: "))
    else:
        print("🏦 The opponent is the banker. 🏦")
        bet = random.randint(1, 1000)
        print(f"💲 Opponent decided to bet ${bet}")

    print(f"💰 Bet set to ${bet}. The game starts now! 💰")
    time.sleep(1)

    print("\n🏦 You (Player) roll your dice:")
    player_dice = roll_dice("Player")

    print("\n🤖 Opponent rolls their dice:")
    opponent_dice = roll_dice("Opponent")

    # Player win/loss checks
    if set(player_dice) == set(winrolls):
        prizemoney = bet * 2
        print("\n🎉 You won with 4-5-6! 🎉")
        print(f"You won ${prizemoney}!")
        if random.choice(opp_choice) == 1:
            print("😡 Opponent got mad! 😡")
            if random.choice(hitmiss) == 1:
                gun()
                print("☠️ Opponent emptied the mag on you. YOU DIED. ☠️")
            else:
                print("😅 He missed. You ran! 🏃💨")
        else:
            print("😤 Opponent took the L silently.")
        return

    elif check_for_doubles(player_dice):
        print("🎉 You rolled doubles! You automatically win! 🎉")
        prizemoney = bet * 3
        print(f"You won ${prizemoney}!")
        swiss_cheese = input("Do you want to Swiss cheese the opponent? (Yes/No): ").strip().capitalize()
        if swiss_cheese == "Yes":
            print("💥 You shot at him... 💥")
            if random.choice(hitmiss) == 1:
                print("🔫 You hit him!")
                gun()
                print("☠️ He died.")
            else:
                print("😬 You missed. He ran.")
        else:
            print("😐 You let him slide...")
        return

    elif set(player_dice) == set(loserolls):
        print("\n😵 You rolled 1-2-3. You lost. 😵")
        swiss_cheese = input("Do you want to Swiss cheese the opponent? (Yes/No): ").strip().capitalize()
        if swiss_cheese == "Yes":
            print("💥 You shot at him... 💥")
            if random.choice(hitmiss) == 1:
                print("🔫 You hit him!")
                gun()
                print("☠️ He died.")
            else:
                print("😬 You missed. He ran.")
        else:
            print("😐 You let him slide...")
        return

    # Opponent win/loss checks
    if set(opponent_dice) == set(winrolls):
        print("\n😵 Opponent won with 4-5-6! You lost. 😵")
        return

    elif check_for_doubles(opponent_dice):
        print("🎉 Opponent rolled doubles! They automatically win! 🎉")
        prizemoney = bet * 3
        print(f"Opponent won ${prizemoney}!")
        swiss_cheese = input("Do you want to Swiss cheese the opponent? (Yes/No): ").strip().capitalize()
        if swiss_cheese == "Yes":
            print("💥 You shot at him... 💥")
            if random.choice(hitmiss) == 1:
                print("🔫 You hit him!")
                gun()
                print("☠️ He died.")
            else:
                print("😬 You missed. He ran.")
        else:
            print("😐 You let him slide...")
        return

    elif set(opponent_dice) == set(loserolls):
        print("\n😵 Opponent rolled 1-2-3. Opponent lost. 😵")
        swiss_cheese = input("Do you want to Swiss cheese the opponent? (Yes/No): ").strip().capitalize()
        if swiss_cheese == "Yes":
            print("💥 You shot at him... 💥")
            if random.choice(hitmiss) == 1:
                print("🔫 You hit him!")
                gun()
                print("☠️ He died.")
            else:
                print("😬 You missed. He ran.")
        else:
            print("😐 You let him slide...")
        return

    print("\n🔁 No win or loss for both players. Rolling again...\n")
    time.sleep(1)
    start_game()

start_game()
