import random

nouns12 = [
    "Tree",
    "Flower",
    "Grass",
    "Mushroom",
    "Cactus",
    "Vine",
    "Coral",
    "Algae",
    "Bush",
    "Shrub"
]

nouns = [
    "Dog",
    "Cat",
    "Elephant",
    "Bird",
    "Fish",
    "Lion",
    "Tiger",
    "Human",
    "Horse",
    "Monkey"
]

verbs = [
    "Ran",
    "Jump",
    "Ate",
    "Slept",
    "Spoke",
    "Wrote",
    "Read",
    "Sang",
    "Danced",
    "Played"
]

adjectives = [
    "Happy",
    "Tall",
    "Bright",
    "Fast",
    "Strong",
    "Beautiful",
    "Smart",
    "Gentle",
    "Loud",
    "Quiet"
]

welcome_1 = input("Welcome to the MADLIBS game. Press enter to continue.")
   

def random_short_story():
    noun = random.choice(nouns)
    not_living_noun = random.choice(nouns12)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
   
    random_story = {
    "noun": noun,
    "noun12": not_living_noun,
    "verb": verb,
    "adj": adjective
}
    return random_story

def show_random_story():
    random_story = random_short_story()
    print("Today's random short story: ")
    print(f"The {random_story['adj']} {random_story['noun']} {random_story['verb']} to the {random_story['noun12']}")
   
if __name__ == "__main__":
    show_random_story()