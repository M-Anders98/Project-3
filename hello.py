from flask import Flask,render_template, request, jsonify, g, session
import urllib.request, json
import http.client
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'wowiezowiesowwieihatethisdamnfasdfl;adsjfasdlkfjadsasdf'
data = {}
# name = ""
# age = 0
# experience = 0


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/recs.html', methods = ["GET", "POST"])
def recs():
    if request.method == "POST":

        # q1
        q1 = request.form.getlist("console")
        # q2
        q2 = request.form.getlist("rating")
        # q3
        q3 = request.form.get("matureContent")
        # q4
        q4 = request.form.getlist("multiplayer")
        # q5
        q5 = request.form.getlist("difficulty")
        # q6
        q6 = request.form.get("time")
        # q7
        q7 = request.form.getlist("structure")
        # q8
        q8 = request.form.get("skills1")
        # q9
        q9 = request.form.get("skills2")
        # q10
        q10 = request.form.get("NPCs")

        q11 = request.form.get("decisionImpacts")

        fullquizanswers = []
        fullquizanswers.append(q1)
        fullquizanswers.append(q2)
        fullquizanswers.append(q3)
        fullquizanswers.append(q4)
        fullquizanswers.append(q5)
        fullquizanswers.append(q6)
        fullquizanswers.append(q7)
        fullquizanswers.append(q8)
        fullquizanswers.append(q9)
        fullquizanswers.append(q10)
        fullquizanswers.append(q11)
        #print(fullquizanswers)
        session['eksdee'] = fullquizanswers

    return render_template('recs.html')

@app.route('/get_data1', methods = ["GET", "POST"])
def api_requests ():

    fullquizanswers = session['eksdee'] 
    print(fullquizanswers)
    q1 = fullquizanswers[0]
    q2 = fullquizanswers[1]
    q3 = fullquizanswers[2]
    q4 = fullquizanswers[3]
    q5 = fullquizanswers[4]
    q6 = fullquizanswers[5]
    q7 = fullquizanswers[6]
    q8 = fullquizanswers[7]
    q9 = fullquizanswers[8]
    q10 = fullquizanswers[9]
    q11 = fullquizanswers[10]
#     Pc = 4
#     xbox one = 1
#     Playstation 4 =18
#     switch = 7
    tags = ""
    genres= ""
    for i in range(len(q1)):
        if q1[i] == "xbox":
            q1[i] = 1
        if q1[i] == "playstaion":
            q1[i] = 18
        if q1[i] == "switch":
            q1[i] = 7
        if q1[i] == "computer":
            q1[i] = 4

    for i in range(len(q2)):
        if q2[i] == "e":
            q2[i] = "everyone"
        if q2[i] == "e10":
            q2[i] = "everyone-10-plus"
        if q2[i] == "t":
            q2[i] = "teen"
        if q2[i] == "m":
            q2[i] = "mature"

    for i in range(len(q4)):
        if q4[i] == "sameConsole":
            q4[i] = "console,"
        if q4[i] == "onlinePlay":
            tags += "multiplayer,"
        if q4[i] == "myself":
            tags += "singleplayer;"
        if q4[i] == "learn2play":
            tags += "multiplayer,"

    if q6 == "3min":
        q6 = 5
    if q6 == "10min":
        q6 = 9
    if q6 == "hour":
        q6 = 14
    if q6 == "hours":
        q6 = 15

    for i in range(len(q7)):
        if q7[i] == "levels":
            tags += "singleplayer,"
        if q7[i] == "stories":
            tags += "story-rich,indie,"
        if q7[i] == "openWorld":
            tags += "open-world,"
        if q7[i] == "campaigns":
            tags += "singleplayer;story-rich,"

    if q8 == "problemSolving":
        genres += "puzzle,role-playing-games-rpg,simulation,strategy,"
    if q8 == "fastReasoning":
        genres += "fighting,sports,shooter,racing,"
    if q8 == "decisionMaking":
        genres += "fighting,racing,simulation,"
    if q8 == "organization":
        genres += "puzzle,simulation,strategy,"


    if q9 == "handeyeCoordination":
        genres += "fighting,puzzle,sports,"
    if q9 == "creativity":
        genres += "simulation,sandbox,"
    if q9 == "logicalThinking":
        genres += "puzzle,strategy,"
    if q9 == "timeManagement":
        genres += "action,arcade,strategy,"
    
    if q10 == "yes10":
        tags += "story-rich"

    if q11 == "popular":
        q11 = "metacritic"
    if q11 == "newness":
        q11 = "released"
    if q11 == "price":
        tags += "f2p,free-to-play"
    if q11 == "expansion":
        dlc = "dlc"
    url = "https://api.rawg.io/api/games?genres="+str(genres)+"&tags="+str(tags)+"&ordering="+str(q11)+"&key=39399cb9ce8f477899ff74f53e93338f"
    print(url)
    response = urllib.request.urlopen(url)
    data = response.read()
    data = json.loads(data.decode('utf-8'))
    gamelist = []
    count = 0
    for x in data["results"]:
            y = json.dumps(x)
            count = 0
            for k in x.values():
                if count == 1:
                    k = k.replace("Director's Cut", "")
                    k = k.replace(" ", "_")
                    k = k.replace(".","")

                    gamelist.append(k)
                count = count + 1
    # countdesc = 0
    # for x in data["results"]:
    #         y = json.dumps(x)
    #         count = 0
    #         for k in x.values():
    #             if count == 5:
    #                 urlwiki = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
    #                 urlwiki = urlwiki + gamelist[countdesc]
    #                 responsewiki = urllib.request.urlopen(urlwiki)
    #                 datawiki = responsewiki.read()
    #                 datawiki = json.loads(datawiki.decode('utf-8'))
    #                 pagenum = list(datawiki['query']['pages'])
    #                 data['results'][2]['background-image'] = datawiki['query']['pages'][pagenum[0]]['extract']
    #                 countdesc += 1
    #             count += 1
    substtring = ""
    for i in range(len(gamelist)):
        gamelist[i] = gamelist[i].encode("ascii", errors="ignore").decode()
        urlwiki = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
        urlwiki = urlwiki + gamelist[i]
        print(urlwiki)
        responsewiki = urllib.request.urlopen(urlwiki)
        datawiki = responsewiki.read()
        datawiki = json.loads(datawiki.decode('utf-8'))
        if 'query' in datawiki:
            pagenum = list(datawiki['query']['pages'])
            print(pagenum[0])
            if 'extract' in datawiki['query']['pages'][pagenum[0]]:
                if(pagenum[0] == -1):
                    substtring = "A game description could not be found. Our apologize while we look into this issue."
                else:
                    substtring = datawiki['query']['pages'][pagenum[0]]['extract']
                    if(len(datawiki['query']['pages'][pagenum[0]]['extract']) < 550):
                        #print("WRONG GAME!")
                        urlwiki = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
                        urlwiki = urlwiki + gamelist[i] + "_(video_game)"
                        responsewiki = urllib.request.urlopen(urlwiki)
                        datawiki = responsewiki.read()
                        datawiki = json.loads(datawiki.decode('utf-8'))
                        pagenum = list(datawiki['query']['pages'])  
                        #print(datawiki['query']['pages'][pagenum[0]]['extract'])
                        if 'extract' in datawiki['query']['pages'][pagenum[0]]:
                            substtring = datawiki['query']['pages'][pagenum[0]]['extract']
                        else:
                            substtring = "A game description could not be found. Our apologize while we look into this issue."
            else:
                substrings = "A game description could not be found. Our apologize while we look into this issue."
            data['results'][i]['background_image'] = substtring[:substtring.find('\n')]
            gamelist[i] = gamelist[i].replace(":", "")
            urlimage = "/images/search?q="+gamelist[i]+"%20game%20cover&count=1"
            conn = http.client.HTTPSConnection("bing-image-search1.p.rapidapi.com")

            headers = {
                'X-RapidAPI-Host': "bing-image-search1.p.rapidapi.com",
                'X-RapidAPI-Key': "d064f5169amsh3d9e48e55e6ef6bp1f606fjsn48921dbaf8b4"
                }

            conn.request("GET", urlimage, headers=headers)

            res = conn.getresponse()
            dataimg = res.read()
            dataimg = json.loads(dataimg.decode("utf-8"))
            imgurl = "<img src="+ dataimg['value'][0]['thumbnailUrl'] + ">"
            print(imgurl)
            data['results'][i]['name'] = data['results'][i]['name'] + "\n " + imgurl
    
    return jsonify(data)


    
@app.route('/index.html')
def home2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
