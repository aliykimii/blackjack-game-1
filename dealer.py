import random

dealer_cards = []
player_cards = []

def deal_cards():
  dealer_cards.append(random.randint(1,11))
  player_cards.append(random.randint(1,11))
 
def draw_cards():
  dealer_cards.append(random.randint(1,11))
