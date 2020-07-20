from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "Nezka"
    current_year = "2020"
    cities = ["Vienna", "Maribor", "Ljubljana"]
    return render_template("index.html", name=name, current_year=current_year, cities=cities)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__== '__main__':
    app.run()