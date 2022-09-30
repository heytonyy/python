from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template('play.html',num=3,bgcolor='blue')

@app.route('/play/<num>')
def level2(num):
    return render_template('play.html',num=int(num),bgcolor='black')

@app.route('/play/<num>/<bgcolor>')
def level3(num,bgcolor):
    return render_template('play.html',num=int(num),bgcolor=bgcolor)

if __name__ == "__main__":
    app.run(debug=True)