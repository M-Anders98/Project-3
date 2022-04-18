from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/recs.html', methods = ["GET", "POST"])
def recs():
    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")
        experience = request.form.get("experience")

        # q1
        q1 = request.form.get("console")
        # q2
        q2 = request.form.get("rating")
        # q3
        q3 = request.form.get("matureContent")
        # q4
        q4 = request.form.get("multiplayer")
        # q5
        q5 = request.form.get("difficulty")
        # q6
        q6 = request.form.get("time")
        # q7
        q7 = request.form.get("structure")
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
