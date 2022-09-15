from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def say_dojo():
    return "Dojo!"

@app.route("/say/<name>")
def name(name):
    return "Hello " + name

@app.route("/repeat/<int:num_of_repetition>/<word>")
def repeat_word(num_of_repetition, word):
    string=""
    for i in range(0, num_of_repetition, 1):
        string+=word+'<br>'
    return string

if __name__ == "__main__":
    app.run(debug=True)