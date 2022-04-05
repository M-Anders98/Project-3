from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/recs.html')
def recs():
    return render_template('recs.html')
    
@app.route('/index.html')
def home2():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
