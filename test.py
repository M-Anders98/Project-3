
import urllib.request, json
url = "https://api.rawg.io/api/games?key=39399cb9ce8f477899ff74f53e93338f"
response = urllib.request.urlopen(url)
data = response.read()
data = json.loads(data.decode('utf-8'))
gamelist = []
count = 0
print(data['results'][1])
print(data['results'][2])
print(data['results'][3])

for x in data["results"]:
    y = json.dumps(x)
    count = 0
    for k in x.values():
        if count == 2:
            k = k.replace(" ", "_")
            gamelist.append(k)
        count = count + 1
print(gamelist)