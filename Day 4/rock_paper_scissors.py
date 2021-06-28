import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("SELAMAT DATANG DI PERMAINAN SUIT JEPANG\n\n")

user_input = int(input("Pilih Pilihanmu : \n 0. Batu\n 1. Gunting\n 2. Kertas\nMasukkan Pilihanmu : "))

comp_input = random.randint(0,2)

if user_input == 0 and comp_input == 0:
  print(rock)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(rock)
  print("\n Hasil : Draw")
  
elif user_input == 0 and comp_input == 1:
  print(rock)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(scissors)
  print("\n Hasil : You Win")

elif user_input == 0 and comp_input == 2:
  print(rock)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(paper)
  print("\n Hasil : You Lose")

elif user_input == 1 and comp_input == 0:
  print(scissors)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(rock)
  print("\n Hasil : You Lose")

elif user_input == 1 and comp_input == 1:
  print(scissors)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(scissors)
  print("\n Hasil : Draw")

elif user_input == 1 and comp_input == 2:
  print(scissors)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(paper)
  print("\n Hasil : You Win")

elif user_input == 2 and comp_input == 0:
  print(paper)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(rock)
  print("\n Hasil : You Win")

elif user_input == 2 and comp_input == 1:
  print(paper)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(scissors)
  print("\n Hasil : You Lose")
elif user_input == 2 and comp_input == 2 :
  print(paper)
  print("Pilihan Komputer : " + str(comp_input) + f"\n")
  print(paper)
  print("\n Hasil : Draw")

else :
  print("INPUT ERROR! PLEASE CHECK YOUR INPUT!")







