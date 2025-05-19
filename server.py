from flask import Flask, render_template


app = Flask(__name__)


@app.route("/ukazka")
def showcase():
	name = "Adam"
	return render_template("index.html", name=name)


@app.route("/about-old")
def about_old():
	return f"<h1>Hello About</h1>"


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/calculator/<int:a>/<b>")
def calculator(a, b):
	b = int(b)
	return render_template("calculator.html", result=a+b)

@app.route("/products")
def products():
	products = [(1, "Mrkev"), (2, "Jabko"), (3, "Avokado"), (4, "Rajče")]
	return render_template("products.html", products=products)

@app.route("/product/<int:id>")
def product(id):
	magic = id % 2
	return render_template("product.html", magic=magic)




if __name__ == "__main__":
	app.run(debug=True, port=5010)