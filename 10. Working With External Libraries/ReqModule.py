import requests
r = requests.get('https://api.github.com/users/daivagnaa')

with open("Daivagna.txt" , "w") as f:
    f.write(r.text)