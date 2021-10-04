from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

transaction = {}

#Step 1 : Print out the logo
print(logo)
print("Welcome to Blind Bidding")

#Step 2 : User input the name and the bid
def user_input() :

  name = input("Enter Your Name : ")
  bid = int(input("How much do you want to bid : Rp. "))

  transaction[name] = bid
 

#Step 3 : Ask the user if there any other user?
def find_highest_bid(bid_record) :
  highest_bid = 0
  winner = ""
  for bidder in bid_record :
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid :
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid amount : Rp. {highest_bid}")


is_continue = False
while not is_continue :
  user_input()
  other_user = input("Is there any other user?")

  if other_user == 'yes' :
    is_continue = False
    clear()

  elif other_user == 'no' :
    is_continue = True
    clear()
    find_highest_bid(transaction)

