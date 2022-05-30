#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from py.prime import makePrime
#from py.galton import galtonboard

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prime/', methods=["GET", "POST"])
def primos():
    if request.method == 'POST':
        n = request.form["num"]
        return render_template("prime.html", list=makePrime(int(n)), title="First " + n + " prime numbers")
    else:
        return render_template("prime.html", list="", title="First prime numbers")


@app.route('/galton/', methods=["GET", "POST"])
def glaton():
    if ((request.method == 'POST') and (request.form["number"] != "") and (int(request.form["number"]) > 1)):
        result = galtonboard(int(request.form["number"]))
        return render_template("galton.html", structure=result[0], URL=result[1])
    else:
        return render_template("galton.html", URL="")

if __name__ == "__main__":
    app.run(debug=True, port=5000)