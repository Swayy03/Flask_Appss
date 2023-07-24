
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'odhcwouhwohdoedoij'

if __name__ == '__app__':
    app.run(debug=True)


@app.route("/login")
def index(): 
    flash("What is your name?")  
    return render_template("index.html")   


@app.route("/gohome", methods=["POST","GET"])
def join():
    flash("Hey " + str(request.form['name_input']) + ", would you like to join your App")
    request.form['name_input']
    return render_template("home.html")