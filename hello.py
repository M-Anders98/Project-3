from flask import Flask,render_template, request, jsonify
import urllib.request, json

import os
app = Flask(__name__)
data = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/get_data1')
def stuff ():
    url = "https://api.rawg.io/api/games?key=39399cb9ce8f477899ff74f53e93338f"
    response = urllib.request.urlopen(url)
    data = response.read()
    data = json.loads(data.decode('utf-8'))
    gamelist = []
    count = 0
    for x in data["results"]:
            y = json.dumps(x)
            count = 0
            for k in x.values():
                if count == 2:
                    k = k.replace(" ", "_")
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
    for i in range(len(gamelist)):
        urlwiki = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
        urlwiki = urlwiki + gamelist[i]
        responsewiki = urllib.request.urlopen(urlwiki)
        datawiki = responsewiki.read()
        datawiki = json.loads(datawiki.decode('utf-8'))
        pagenum = list(datawiki['query']['pages'])
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
            substtring = datawiki['query']['pages'][pagenum[0]]['extract']
        data['results'][i]['background_image'] = substtring[:substtring.find('\n')]


    

    return jsonify(data)


@app.route('/recs.html', methods = ["GET", "POST"])
def recs():
    
    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")
        experience = request.form.get("experience")

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
        print(age, experience, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
   
    return render_template('recs.html')
    
@app.route('/index.html')
def home2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
