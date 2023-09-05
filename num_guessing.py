import random
num = [1,2,3,4,5,6,7,8,9,10]
a = input("enter your choice: ")
b = random.choice(num)
if a==b:
    print(f"woah, it's {b} so you won the match")
else:
    print(f"sorry I have {b} so yeah you get it right, you lost to me!")