import random


card_pile = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0


## choose two random cards from the deck. Cards are not removed from the deck as they are drawn.
def deal_cards(cards, how_many):
    for i in range(how_many):
        card = random.choice(card_pile)
        cards.append(card)

    return card

def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0

    return score



#draw 2 cards for both user and computer
deal_cards(cards = user_cards, how_many = 2)
deal_cards(cards = computer_cards, how_many = 2)
calculate_score(cards = user_cards)
calculate_score(cards = computer_cards)
print(user_cards)
print(user_score)
print(computer_score)
print(f"{random.choice(computer_cards)} and one unknown")

if user_score > 21:
    if 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
        user_score -= 10
        if user_score > 21:
            print("You lost")








