import random


card_pile = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0


def deal_cards(cards, how_many):
    """choose two random cards from the deck. Cards are not removed from the deck as they are drawn."""
    for i in range(how_many):
        card = random.choice(card_pile)
        cards.append(card)
    return card


def calculate_score(cards):
    """sumarize the score from cards"""
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        if 11 in user_cards:
            if score > 21:
                cards.remove(11)
                cards.append(1)
                score -= 10
        return 0
    return score



#draw 2 cards for both user and computer
deal_cards(cards = user_cards, how_many = 2)
deal_cards(cards = computer_cards, how_many = 2)
calculate_score(cards = user_cards)
calculate_score(cards = computer_cards)

#show your cards and one of computers
print(user_cards)
print(f"{random.choice(computer_cards)} and one unknown")

#set the score
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0:
    print("You lost!")
elif computer_score == 0:
    print("You won!")
else:
    another_one = input("Do you want to draw another card? Press 'y' for yes or 'n' for no: ")
    if another_one in ["y", "Y"]:
        deal_cards(cards = user_cards, how_many = 1)
    else:
        print("Game over!")








