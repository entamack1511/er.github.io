from flask import Flask, flash, redirect, render_template, request, session




app = Flask(__name__)


@app.route("/")
def prompt():
    return render_template("Begin.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/results")
def results():
    return render_template("results.html")