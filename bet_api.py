import json 
import requests 

api_key = "YOUR_API_KEY" #for getting api key visit https://api.betting-api.com
headers = {"Authorization": api_key}
url1 = "https://api.betting-api.com/1xbet/football/line/league/39969/matches"
url3 = "https://api.betting-api.com/1xbet/football/live/leagues"
url5 = "https://api.betting-api.com/1xbet/football/live/all"
url7 = "https://api.betting-api.com/1xbet/football/line/all"
url8 = "https://api.betting-api.com/1xbet/football/line/leagues"
url9 = "https://api.betting-api.com/1xbet/football/info"

print("URL1 Response")
for i in range(3):
    req = requests.get(url1, headers=headers)
    if req.status_code == 200:
        data = req.json()
        print(f"League : {data[i]['title']}")
        print("Team 1's Infos")            
        print(f"Team 1 : {data[i]['team1']}")
        print(f"Team 1's id : {data[i]['team1_id']}")
        print("Team 2's Infos")
        print(f"Team 2 : {data[i]['team2']}")
        print(f"Team 2's id : {data[i]['team2_id']}")
        print(f"Match Score {data[i]['team1']} : {data[i]['score1']} - {data[i]['team2']} : {data[i]['score2']}")

print("URL3 Response")
for i in range(3):
    req = requests.get(url3, headers = headers)
    if req.status_code == 200:
        data = req.json()
        print(f"Title : {data[i]['title']}")
        print(f"Title Rus : {data[i]['title_rus']}")            
        print(f"Is Cyber ? : {data[i]['isCyber']}")
        print(f"Is Simulated ? : {data[i]['isSimulated']}")
        print(f"League Id  : {data[i]['league_id']}")

print("URL5 Response")
for i in range(3):
    req = requests.get(url5, headers=headers)
    if req.status_code == 200:
        data = req.json()
        print(f"League : {data[i]['title']}")
        print("Team 1's Infos")            
        print(f"Team 1 : {data[i]['team1']}")
        print(f"Team 1's id : {data[i]['team1_id']}")
        print("Team 2's Infos")
        print(f"Team 2 : {data[i]['team2']}")
        print(f"Team 2's id : {data[i]['team2_id']}")
        print(f"Match Score {data[i]['team1']} : {data[i]['score1']} - {data[i]['team2']} : {data[i]['score2']}")

print("URL7 Response")
for i in range(3):
    req = requests.get(url7, headers=headers)
    if req.status_code == 200:
        data = req.json()
        print(f"League : {data[i]['title']}")
        print("Team 1's Infos")            
        print(f"Team 1 : {data[i]['team1']}")
        print(f"Team 1's id : {data[i]['team1_id']}")
        print("Team 2's Infos")
        print(f"Team 2 : {data[i]['team2']}")
        print(f"Team 2's id : {data[i]['team2_id']}")
        print(f"Match Score {data[i]['team1']} : {data[i]['score1']} - {data[i]['team2']} : {data[i]['score2']}")
                
print("URL8 Response")                
for i in range(3):
    req = requests.get(url8, headers = headers)
    if req.status_code == 200:
        data = req.json()
        print(f"Title : {data[i]['title']}")
        print(f"Title Rus : {data[i]['title_rus']}")            
        print(f"Is Cyber ? : {data[i]['isCyber']}")
        print(f"Is Simulated ? : {data[i]['isSimulated']}")
        print(f"League Id  : {data[i]['league_id']}")
        print(f"Country Id : {data[i]['country_id']}")        

print("Server Infos")
req = requests.get(url9, headers=headers)
data = req.json()
print(data)