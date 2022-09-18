from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")	



@app.route('/<int:numbers>')
def eightByFour(numbers):
    return render_template("index2.html", numbers=numbers)




@app.route('/<int:number1>/<int:number2>')
def numberBynumber(number1,number2):
    return render_template("index3.html", x=number1, y= number2)



if __name__=="__main__":
    app.run(debug=True)