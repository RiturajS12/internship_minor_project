import random
while True:
   a = input("Please enter your guess: ").lower()
   if a=="7up" or a=="7down":
     break
rnd = random.randint(2,13)
if rnd>=7:
   if a=="7up":
     print("You won")
   else:
     print("You loose")
else:
   if a=="7down":
     print("You won")
   else:
     print("You loose")
