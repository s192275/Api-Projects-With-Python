import requests
import json
#This code contains getting requests from basic api site and this site generates random users and informations
url = "https://randomuser.me/api"
for i in range(200):
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"{i}th User Infos")
        print(f"Name : {data['results'][0]['name']['title']} {data['results'][0]['name']['first']} {data['results'][0]['name']['last']}")    
        print(f"Gender: {data['results'][0]['gender']}")
        print(f"Location : {data['results'][0]['location']['street']['name']} Street {data['results'][0]['location']['city']} City {data['results'][0]['location']['state']} State / {data['results'][0]['location']['country']}")
        print("Coordinates")
        print(f"Longtitude : {data['results'][0]['location']['coordinates']['longitude']} Latitude : {data['results'][0]['location']['coordinates']['latitude']}")
        print(f"Email : {data['results'][0]['email']}")
        print(f"Username : {data['results'][0]['login']['username']}")
        print(f"Password : {data['results'][0]['login']['password']}")
        print(f"Picture : {data['results'][0]['picture']['medium']}")
    else:
        print(f"Error : {req.status_code}")    
