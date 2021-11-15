import random
import os
import art


def deal_cards(cards, how_many):
    """choose two random cards from the deck. Cards are not removed from the deck as they are drawn."""
    card_pile = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(how_many):
        card = random.choice(card_pile)
        cards.append(card)
    return card


def calculate_score(cards):
    """sumarize the score from cards"""
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score


def compare(user_score, computer_score):
    """compare the scores of user and computer"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack!!!"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def game():
    """plays the game"""
    print(art.logo)
    is_game_over = False
    user_cards = []
    computer_cards = []

    #draw 2 cards for both user and computer
    deal_cards(cards = user_cards, how_many = 2)
    deal_cards(cards = computer_cards, how_many = 2)

    while not is_game_over:
        #set the score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        #show your cards and one of computers
        print(f"Your cards are: {user_cards}. Current score: {user_score}")
        print(f"Computer has: {random.choice(computer_cards)} and one unknown")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_one = input("Do you want to draw another card? Press 'y' for yes or 'n' for no: ")
            if another_one in ["y", "Y"]:
                deal_cards(cards = user_cards, how_many = 1)
                user_score = calculate_score(cards = user_cards)
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            deal_cards(cards = computer_cards, how_many = 1)
            computer_score = calculate_score(computer_cards)

    print(f"Your final cards are: {user_cards}. Final score: {user_score}")
    print(f"Computers final cards are: {computer_cards}. Computer score: {computer_score}")
    print(compare(user_score = user_score, computer_score = computer_score))

    while input("Do you want to play again?") in ["Y", "y"]:
        clean = lambda: os.system('cls')
        clean()
        game()


game()




