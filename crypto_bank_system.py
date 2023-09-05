import requests
amount = int(input("enter the amount: "))
a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
price = a['bpi']['USD']['rate']
out = amount/float(price.replace(",",""))
print(f"You got {out} BTC at price of {price}")
b = ['kunal','jeki','garvit']
c = input("please enter your login name: ")
if c==b[0]:
    d =int(input("enter your password: "))
    if d==123456:
        print("you're logged in")
        print("you have 0 BTC & 100USD please proceed to buy BTC!")
        a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = a['bpi']['USD']['rate']
        e=int(input('enter the USD amount to buy BTC: '))
        out = e/float(price.replace(",",""))
        BTC= out
        USD=int(100)-int(e)
        print(f'you have now {BTC} BTC and {USD} USD')
    else:
        print("password is wrong so please try again")
elif c==b[1]:
    d = int(input("enter your password: "))
    if d==123457:
        print("you're logged in")
        print("you have 0 BTC & 100USD")
        e=input('enter the USD amount to buy BTC: ')
        a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = a['bpi']['USD']['rate']
        out = e/float(price.replace(",",""))
        BTC= out
        USD=int(100)-int(e)
        print(f'you have now {BTC} BTC and {USD} USD')
    else:
        print("password is wrong so please try again")
elif c==b[2]:
    d = int(input("enter your password: "))
    if d==9123456:
        print("you're logged in")
        print("you have 0 BTC & 100USD") 
        e=int(input('enter the USD amount to buy BTC: '))
        a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = a['bpi']['USD']['rate']
        out = e/float(price.replace(",",""))
        BTC= out
        USD=int(100)-int(e)
        print(f'you have now {BTC} BTC and {USD} USD')
    else:
        print("password is wrong so please try again")
else:
    print('user not available,try to log in with valid username')