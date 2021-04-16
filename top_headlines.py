import requests 
import json
from flask import Flask, render_template
import secrets

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome!</h1>"

@app.route('/name/<nm>')
def usr_name(nm):
    return render_template("name.html", name =nm)

@app.route('/headlines/<nm>')
def find_tech(nm):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    API_key = secrets.NYT_API_KEY
    params = {"api-key":API_key}
    results = requests.get(baseurl, params=params).json()
    headline_list = []
    i = 0
    for ele in results["results"]:
        if i < 5:
            headline_list.append(ele["title"])
            i += 1
    return render_template("headlines.html",headlines = headline_list, name=nm)

@app.route('/links/<nm>')
def find_link(nm):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    API_key = secrets.NYT_API_KEY
    params = {"api-key":API_key}
    results = requests.get(baseurl, params=params).json()
    link_list = {}
    i = 0
    for ele in results["results"]:
        if i < 5:
            #headline_list.append(ele["title"])
            link_list[ele["title"]] = ele["url"]
            i += 1
    return render_template("links.html", links = link_list, name=nm)

@app.route('/images/<nm>')
def find_image(nm):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    API_key = secrets.NYT_API_KEY
    params = {"api-key":API_key}
    results = requests.get(baseurl, params=params).json()
    image_list = []
    i = 0
    for ele in results["results"]:
        if i < 5:
            #headline_list.append(ele["title"])
            image_list.append(ele["url"])
            image_list.append(ele["title"])
            image_list.append(ele["multimedia"][0]["url"])
            i += 1
    return render_template("images.html", images = image_list, name=nm)        


if __name__ == "__main__":
    print("launching the flask app", app.name)
    app.run(debug=True)
