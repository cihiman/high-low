from game_data import data
from art import logo
from art import vs
from replit import clear
import random

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, {desc} from {country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    while game_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
        print(f"Účet A: {format_data(account_a)}")
        print(vs)
        print(f"Účet B: {format_data(account_b)}")

        guess = input("Kdo má více followerů, A nebo B? : ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)


        if is_correct:
            clear()
            print(logo)
            score += 1
            print("*" * 40)
            print(f"Správná odpověď! Aktuální skóre: {score}")
            print("*" * 40)
        else:
            game_continue = False
            print("_" * 40)
            print(f"Špatná odpověď! Konečné skóre: {score}")
            print("_" * 40)
            

game()
