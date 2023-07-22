
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'odhcwouhwohdoedoij'

if __name__ == '__app__':
    app.run(debug=True)



@app.route("/hello")
def index(): 
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hey " + str(request.form['name_input']) + ", great to see you")
    request.form['name_input']
    return render_template("index.html")