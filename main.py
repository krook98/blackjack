import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    ## choose two random cards from the deck. Cards are not removed from the deck as they are drawn.
    for i in range(2):
        card = random.choice(cards)
        user_cards.append(card)
        user_score += card
    for i in range(2):
        card = random.choice(cards)
        computer_cards.append(card)
        computer_score += card


deal_cards()




