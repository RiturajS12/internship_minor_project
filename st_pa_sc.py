import random

lst = ["stone", "paper", "scissor"]
a = input("Please Enter your choice").lower()
rno = random.choice(lst)
print(f"CPU Choose {rno}")
print(f"You Choosed {a}")
if a==rno:
   print("Game Tie")
elif (a==lst[1] and rno==lst[0] ) or (a==lst[2] and rno==lst[1] ) or (a==lst[0] and rno==lst[2] ) :
   print("You won")
else:
   print("You loose")