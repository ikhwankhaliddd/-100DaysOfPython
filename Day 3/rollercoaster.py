print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120 :
  print("You can ride this roller coaster, Enjoy!")
  age = int(input("How old are you?"))
  if age > 18 :
    print("You have to pay $12")
  
  elif age >= 12 and age <= 18:
    print("You have to pay $7")

  else : 
    print("You have to pay $5")

else :
  print("Sorry, You cant ride")
