from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", times=3, color='blue')	




@app.route('/playground/<int:times>/<color>')
def play(times, color):
    return render_template("index.html", times=times, color=color)

if __name__=="__main__":
    app.run(debug=True)