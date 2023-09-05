a = input("enter first no.: ")
operator = input("enter operator(+,-,*,/,%): ")
b = input("enter second no.: ")
if operator == "+":
    print(int(a) + int(b))
elif operator == "-":
    print(int(a) - int(b))
elif operator == "*":
    print(int(a) * int(b))
elif operator == "/":
    print(int(a) / int(b))
    try:
        print(0/0)
    except:
        print("zero can't be divide by zero")
elif operator == "%":
    print(int(a) % int(b))
else:
    print("ERROR")