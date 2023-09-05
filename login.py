#import random
#st = "stone"
#pa = "paper"
#sc = "scissor"
#a = input("enter your choice(st,pa,sc): ")
#elements = ['st', 'pa', 'sc']
#b = random.choice(elements)
#if a==b:
#    print("draw")
#elif a==st:
#    if b==pa:
#        print("paper, lost")
#    else:
#        print("scissor, won")
#elif a==pa:
#    if b==st:
#        print("stone, won")
#    else:
#        print("scissor, lost")
#elif a==sc:
#    if b==st:
#        print("stone, lost")
#    else:
#        print("paper, won")

import requests
# amount = int(input("enter the amount: "))
# a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
# price = a['bpi']['USD']['rate']
# out = amount/float(price.replace(",",""))
# print(f"You got {out} BTC at price of {price}")
user ={ 1:{'username':'Admin@123','pass':'123','Balance':'100 USD','BTC B':0,'Name':'Garvit'}, 2:{'username':'User@a','pass':'a','Balance':'120 USD','BTC B':1,'Name':'Aditya'}, 3:{'username':'User@b','pass':'b','Balance':'50 USD','BTC B':2,'Name':'Kunal'}}
userid = None
while userid==None:
    uname=input("please enter your username: ")
    Pass=input("please enter your password: ")
    for i in range(1,4):
        if user[i]['username']==uname and user[i]['pass']==Pass:
            userid=i
            break
print(f"hey {user[userid]['Name']} you have {user[userid]['Balance']} USD & {user[userid]['BTC B']} BTC ")

request ={1:{'b':'requests.get("https://flask-internship.iamkunal9.repl.co/").json()'},
2:{'c':'requests.post("https://flask-internship.iamkunal9.repl.co/").json()'}}
req=None
while req==None:
    d = input("enter 1 to fetch the message,enter 2 to send the message,enter 3 to exit: ")
    for i in range(1,3):
        if request[i]['b']==d or request[i]['c']==d:
            request=i
            break

