#blackjack
import time
import random
playercards = []
botcards = []
cards = [
    ("Ace", 11), ("Ace", 11), ("Ace", 11), ("Ace", 11),
    ("Jack", 10), ("Jack", 10), ("Jack", 10), ("Jack", 10),
    ("Queen", 10), ("Queen", 10), ("Queen", 10), ("Queen", 10),
    ("King", 10), ("King", 10), ("King", 10), ("King", 10),
    ("2", 2), ("2", 2), ("2", 2), ("2", 2),
    ("3", 3), ("3", 3), ("3", 3), ("3", 3),
    ("4", 4), ("4", 4), ("4", 4), ("4", 4),
    ("5", 5), ("5", 5), ("5", 5), ("5", 5),
    ("6", 6), ("6", 6), ("6", 6), ("6", 6),
    ("7", 7), ("7", 7), ("7", 7), ("7", 7),
    ("8", 8), ("8", 8), ("8", 8), ("8", 8),
    ("9", 9), ("9", 9), ("9", 9), ("9", 9),
    ("10", 10), ("10", 10), ("10", 10), ("10", 10)
]
card_values = {
    "Ace": 11, "King": 10, "Queen": 10, "Jack": 10,
    "10": 10, "9": 9, "8": 8, "7": 7,
    "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

def playercard():
    while len(playercards) < 2:
        print("...")
        time.sleep(1)
        card = random.choice(cards)
        name, _ = card
        cards.remove(card)

        if name == "Ace":
            while True:
                val = input("You got an Ace! Choose its value (1 or 11): ").strip()
                if val == "1":
                    playercards.append("Ace1")  # Ace as 1
                    break
                elif val == "11":
                    playercards.append("Ace")   # Ace as 11
                    break
                else:
                    print("Please enter 1 or 11.")
        else:
            playercards.append(name)

        print(f"Dealer passed you a {name}")
        print(playercards)

    while True:
        # Calculate total treating "Ace1" as 1 and "Ace" as 11
        playertotal = 0
        for card in playercards:
            if card == "Ace1":
                playertotal += 1
            else:
                playertotal += card_values[card]

        if playertotal == 21:
            print(f"Your final hand: {playercards}")
            print(f"Total: {playertotal}")
            print("Blackjack! You win! 🎉")
            return playertotal
        if playertotal > 21:
            print(f"Your final hand: {playercards}")
            print(f"Total: {playertotal}")
            print("Over 21, you lose.")
            return 0
        more = input("Another card? (Yes/No): ").capitalize().strip()
        if more == "Yes":
            print("...")
            time.sleep(1)
            card = random.choice(cards)
            name, _ = card
            cards.remove(card)

            if name == "Ace":
                while True:
                    val = input("You got an Ace! Choose its value (1 or 11): ").strip()
                    if val == "1":
                        playercards.append("Ace1")
                        break
                    elif val == "11":
                        playercards.append("Ace")
                        break
                    else:
                        print("Please enter 1 or 11.")
            else:
                playercards.append(name)

            print(f"Dealer passed you a {name}")
            print(f"Your cards: {playercards}")
        elif more == "No":
            print(f"Your final hand: {playercards}")
            print(f"Total: {playertotal}")
            if playertotal < 16:
                print("Under 16, you lose.")
                return 0
            return playertotal
        else:
            print("Please answer Yes or No.")

def botcard():
    print("Dealer receiving his cards...")
    time.sleep(2)
    while len(botcards) < 2:
        card = random.choice(cards)
        name, _ = card
        botcards.append(name)
        cards.remove(card)

    while True:
        bottotal = sum(card_values[card] for card in botcards)
        if bottotal == 21:
            print(f"Dealer's cards: {botcards}")
            print(f"Total: {bottotal}")
            print("Dealer hits 21. Dealer wins!")
            return bottotal
        if bottotal > 21:
            print(f"Dealer's cards: {botcards}")
            print(f"Total: {bottotal}")
            print("Dealer busts. You win! 🎉")
            return 0
        if bottotal < 15:
            print("Dealer taking another card...")
            time.sleep(1)
            card = random.choice(cards)
            name, _ = card
            botcards.append(name)
            cards.remove(card)
        else:
            print("Dealer has taken his final hand...")
            print(f"Dealer's cards: {botcards}")
            print(f"Total: {bottotal}")
            return bottotal

# Play both hands
playertotal = playercard()
if playertotal:
    bottotal = botcard()
    if bottotal:
        if playertotal > bottotal:
            print("You win! 🎉")
        elif bottotal > playertotal:
            print("Dealer wins.")
        else:
            print("It's a draw.")
