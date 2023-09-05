import requests

def getData(username):
  data = []
  d = requests.get("https://flask-internship.iamkunal9.repl.co/getdata").json()
  for i in d:
    if i["to"]==username:
      data.append(i)
  if len(data)>0:
    for j in data:
      print(f"From: {j['from']}\nMessage: {j['message']}")
  else:
    print("No message found")
def postData(username):
  to = input("Enter username whom you want to send message: ")
  message = input("Enter Message: ")
  data = {
    'from':username,
    'to':to,
    'message':message
  }
  resp = requests.post("https://flask-internship.iamkunal9.repl.co/postdata",json=data).json()
  if resp['success']=="ok":
    print("Data sent successfully")
  else:
    print("Error while sending")

userid = None
userdata = {
  1:{
    "username":"iamkunal9",
    "password":"whoami",
  },
  2:{
    "username":"harshyadav",
    "password":"kuchbhi",
  },
  3:{
    "username":"muskaann.29",
    "password":"Sotu@123",
  },
  4:{
    "username":"ishajain",
    "password":"isha12",
},
  5:{
    "username":"kalika123",
    "password":"kalika2",
  },
  6:{
    "username":"kritig20",
    "password":"kayy2",
  },  
  7:{
    "username":"RituRAjs12",
    "password":"kyundu",
  },
  8:{'username':'Aditya@2',
     'password':'A2',
    }
}

while userid==None:
  uname = input("Enter UserName")
  passwd = input("Enter Password")
  for i in userdata:
    if userdata[i]['username'] == uname and userdata[i]['password'] == passwd:
      userid = i
      break
username = userdata[userid]['username']
print(f"Logged in as {username}")
while True:
  inpt = input("Enter 1 to fetch new chat\nEnter 2 to send message\Enter 3 to exit\n")
  match inpt:
    case "1":
      getData(username)
    case "2":
      postData(username)
    case "3":
      exit()
    case default:
      print("Invalid Input")
  
      
  