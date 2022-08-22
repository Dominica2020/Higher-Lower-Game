# TO DO LIST
# Generate random print "Compare A" + "Against B"
    # print name, description, country
# Compare follower count
# Track score
# If guess correct:
    # increase score
    # A now becomes B
# If guess wrong:
    # quit came & display final score

from random import randint
from art import logo, vs
from game_data import data
from replit import clear

def random_index():
    return randint(0, 49)

def celeb_details_a():
    ''' Function returns 1st celeb details (Compare A initially)
    '''
    a_index = random_index()
    a_name = data[a_index]["name"]
    a_description = data[a_index]["description"]
    a_country = data[a_index]["country"]
    a_followers = data[a_index]["follower_count"]
    return f"{a_name}, a {a_description}, from {a_country}.", a_followers

def celeb_details_b():
    ''' Function returns 2nd celeb details (Against B initially)
    '''
    b_index = random_index()
    b_name = data[b_index]["name"]
    b_description = data[b_index]["description"]
    b_country = data[b_index]["country"]
    b_followers = data[b_index]["follower_count"]
    return f"{b_name}, a {b_description}, from {b_country}.", b_followers,

def game():
    score = 0
    play = True
    while play:
        if score == 0:
            print(logo)
            celeb_a = celeb_details_a()
            print(f"Compare A: {celeb_a[0]}")
            print("")
            print(vs)
            celeb_b = celeb_details_b()
            print(f"Compare B: {celeb_b[0]}")
            print("------")
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()
            clear()
        else:
            print(logo)
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {celeb_b[0]}")
            print("")
            print(vs)
            celeb_b = celeb_details_b()
            print(f"Compare B: {celeb_b[0]}")
            print("------")
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()
            clear()
        if guess == "A" and celeb_a[1] > celeb_b[1]:
            score += 1
        elif guess == "B" and celeb_b[1] > celeb_a[1]:
            score += 1
        else:
            print(f"Oops, that's wrong. Final score: {score}")
            play = False

game()
