import random
import time

athome12 = [1, 2]  # 1 = owner home, 2 = not home
come_dontcome = [1, 2]  # 1 = opp comes out, 2 = doesn't
hit_miss = [1, 2]  # 1 = hit, 2 = miss
houses = [1, 2, 3, 4, 5]
yesanswers = ["Ye", "Yes"]
noanswers = ["Nah", "No"]
profit = range(0, 4000)
ammo = 0  # starting empty


def cashearn():
    cash = random.choice(profit)
    if cash < 1000:
        print("Lil ahh lick")
    elif cash < 2000:
        print("you got a band ")
    elif cash < 3000:
        print(" you got 2 bands ")
    elif cash < 4000:
        print(" you got 3 bands ")
    else:
        print(" you got 4 bands ")
    print(f"Balance: ${cash}")


def reload_mag():
    global ammo
    while ammo < 8:
        time.sleep(0.5)
        ammo += 1
        print(f"Reloading... Ammo: {ammo}/8")
    print("Magazine full, hit a lick.")


def shoot():
    global ammo
    if ammo > 0:
        ammo -= 1
        print(f"You bust a shot. Ammo left: {ammo}/8")
        outcome = random.choice(hit_miss)
        if outcome == 1:
            print("You hit him! 💥")
            emptymag = input("Empty mag on him? (Ye/Nah): ").capitalize()
            while ammo > 0 and emptymag in yesanswers:
                time.sleep(0.3)
                ammo -= 1
                print(f"POP💥 Ammo left: {ammo}/8")
            if ammo == 0:
                print("Mag is empty. Time to reload.")
        else:
            print("You missed! He ran to tell his gang 🏃")
    else:
        print("Click! No ammo left.")
        choice = input("Reload? (Ye/Nah): ").capitalize()
        if choice in yesanswers:
            reload_mag()
        else:
            print("Empty blick 😐")


def enuf_ammo():
    global ammo
    if ammo <= 0:
        print("No ammo, reloading...")
        reload_mag()
    else:
        print(f"You got {ammo}/8 in the mag.")


def at_home_status():
    return random.choice(athome12)


def at_home_house():
    return random.choice(houses)


def main_slide_house():
    enuf_ammo()

    owner_home = at_home_house()
    owner_status = at_home_status()

    while True:
        try:
            attack = int(input("Pick a house to lick (1-5): "))
            if 1 <= attack <= 5:
                break
            else:
                print("Error — pick between 1 and 5.")
        except:
            print("Enter a valid number.")

    if attack == owner_home and owner_status == 1:
        print("Owner home — Run🏃🏃🏃")
    else:
        print("Sliding on the house...")
        time.sleep(3)
        print("House licked successfully ")
        cashearn()
        cordc()


def cordc():
    kdkd = random.choice(come_dontcome)
    if kdkd == 1:
        print("Your opp spotted you on the block. 🔫")
        ynshoot = input("Shoot him or nah? (Ye/Nah): ").capitalize()
        if ynshoot in yesanswers:
            shoot()
        else:
            print("You let him slide... risky.")


if __name__ == "__main__":
    main_slide_house()
