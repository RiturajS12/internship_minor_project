import random
lttry = []
while True: 
    a = input("Please enter your name")
    if a.lower()!= "exit":
        lttry.append(a)
    else:
        rnd = random.randint(0, len(lttry))
        print(f"Winner is {lttry[rnd]}")
    break