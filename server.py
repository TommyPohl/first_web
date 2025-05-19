from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "Adam"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return "<h1>Hello About</h1>"


if __name__ == "__main__":
    app.run(debug=True)