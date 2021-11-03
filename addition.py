import dealer

def dealer_sum():
  result = sum(dealer.dealer_cards)
  if result > 21 and 11 in dealer.dealer_cards:
       dealer.dealer_cards.append(int(1))
       dealer.dealer_cards.remove(int(11))
       result = sum(dealer.dealer_cards)
  return result

def player_sum():
  result = sum(dealer.player_cards)
  if result > 21 and 11 in dealer.player_cards:
       dealer.player_cards.append(int(1))
       dealer.player_cards.remove(int(11))
       result = sum(dealer.player_cards)
  return result
