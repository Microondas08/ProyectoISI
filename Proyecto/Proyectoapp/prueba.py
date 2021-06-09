import requests

url = "https://instagram47.p.rapidapi.com/search"

querystring = {"search":"antonio10ms"}

headers = {
    'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
    'x-rapidapi-host': "instagram47.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



print(response.json()["body"]["users"])

print(len(response.json()["body"]["users"]))

json = response.json()["body"]["users"]

for i in range(len(response.json()["body"]["users"])):
    print(response.json()["body"]["users"][i])
    print('\n')
    print(json[i].keys())

    if json[i]["user"]["username"]=="antonio10ms":
        foto = json[i]["user"]["profile_pic_url"]


print (foto)