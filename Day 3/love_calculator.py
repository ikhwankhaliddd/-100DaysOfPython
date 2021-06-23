# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_string = name1 + name2
lower_name = combine_string.lower()


t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')
l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')


total1 = t + r + u + e 
total2 = l + o + v + e
out = str(total1)+str(total2)

if out < "10" or out > "90" :
  print(f"Your score is {out}, you go together like coke and mentos.")


elif out >="40" and out <= "50" :
  print(f"Your score is {out}, you are alright together")


else :
  print(f"Your score is {out}.")