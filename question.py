import dealer
import addition

def user_response():
  response = input("Do you want to hit or stand? ")

  if response == "hit":
    return f"{response}"
    
  elif response == "stand":
    return f"{response}"

  else:
    return "the response is not correct"

def partial_result():
  print(f"Dealer cards is {dealer.dealer_cards[0]}")

  print(f"Player card = {dealer.player_cards} , total = {addition.player_sum()}")

def full_result():
  print(f"Dealer cards is = {dealer.dealer_cards} , Dealer sum = {addition.dealer_sum()} \nPlayer card = {dealer.player_cards} , Player sum = {addition.player_sum()}")
