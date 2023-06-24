"""
movie web app - a python 3 Flask web app to fetch movie review data
"""

__author__ = "Chris Bidlake, Danny Deringer, Lata Gadoo, Jayasri Puppala, Mercy Isaac"
__copyright__ = "Copyright (c) Chris Bidlake, 2023"
__license__ = "GNU GPL3"

# imports
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

#decorator to access the app
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

#decorator to access the service
@app.route("/eval_review", methods=['GET', 'POST'])
def reviewclassify():

    #extract form inputs
    review = request.form.get("review")

    #url for movie model app
    url = "https://movie-model-app-4a8064e53e24.herokuapp.com/api/eval"
  
    #post data to url
    response =  requests.get(url, json=json.dumps(review))

    #send input values and prediction result to index.html for display
    return render_template("index.html", review = review,  results=response.text)
  