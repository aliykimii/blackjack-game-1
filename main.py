import addition
import dealer
import art
import question


def comparing_results(dealer_cards,player_cards):
  if dealer_cards == 21 and player_cards  == 21:
    print("Push")
    question.full_result()
    
  elif player_cards == 21:
    question.full_result
    print("You have a blackjack. Congratulations!You Win!!")

  elif dealer_cards == 21:
    question.full_result()
    print("The Dealer has the blackjack.. You lose") 
    
  elif dealer_cards > 21:
    question.full_result()
    print("Dealer's cards is over than 21. You win")
    
  elif player_cards > 21:
    question.full_result()
    print("Your card is over than 21. The Dealer wins")

  elif player_cards > dealer_cards:
    question.full_result()
    print("Congratulatios!! You win") 

  elif dealer_cards > player_cards:
    question.full_result()
    print("You lose..Better luck next time")

  elif dealer_cards == player_cards:
    question.full_result()
    print("push")
       
     

#Print the logo and add first 2 card
def game_start():
  print(art.logo)
  for i in range(2):
    dealer.deal_cards()
  question.partial_result()
game_start()

 
while True:
  player_response = question.user_response()

  if player_response == "hit":
    dealer.deal_cards()
    question.partial_result()

  elif player_response == "stand":
    while addition.dealer_sum()  < 17:
      dealer.draw_cards()
    comparing_results(addition.dealer_sum(),addition.player_sum())
    break

  


