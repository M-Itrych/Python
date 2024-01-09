import random
from art import logo

def clear():
    """
    'Clears' the commandline
    :return: None
    """
    print("\n" * 100)


def deal_card():
    """
    Returns a random card from the cards list
    :return: Int
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    Calculates the score of a hand and returns the sum of all the values in the hand.
    If the hand is blackjack, then it will return 0.
    Also, if card is an ace, and it's over 21 it will change it to 1 instead of 11
    :param cards: List of cards
    :return: Int
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)


def compare(user_s, computer__s):
    if user_s == computer__s:
        return "Draw!"
    elif computer__s == 0:
        return "Lose, opponent has Blackjack!"
    elif user_s == 0:
        return "Win with a Blackjack"
    elif user_s > 21:
        return "You went over. You lose!"
    elif computer__s > 21:
        return "Opponent went over. You lose!"
    elif user_s > computer__s:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = -1
    computer_score = -1

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {user_cards}, final score: {user_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()