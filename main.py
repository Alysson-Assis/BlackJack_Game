import random
from art import logo
def clear():
    import os
    os.system('clear') or None


def dealer():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compare the cards and shows who's the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    computer_cards = []
    user_cards = []
    game_is_on = True

    for cards_game in range(2):
        user_cards.append(dealer())
        computer_cards.append(dealer())

    while game_is_on:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on = False
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                user_cards.append(dealer())
            else:
                game_is_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealer())
        computer_score = calc_score(computer_cards)

    print(f"    Your final hand: {user_cards}, current score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

