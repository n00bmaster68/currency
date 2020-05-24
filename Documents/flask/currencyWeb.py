from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("currency.html")

@app.route("/convert", methods=["POST"])
def convert():
	base = request.form.get("base")
	symbols = request.form.get("symbols")
	base = base.upper()
	symbols = symbols.upper()
	res = requests.get("https://api.exchangeratesapi.io/latest?", params={"base": base, "symbols": symbols})

	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful")
	data = res.json()
	rate = data["rates"][symbols]
	return render_template("convert.html", base=base, rate=rate, symbols=symbols)