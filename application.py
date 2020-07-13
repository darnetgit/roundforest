import requests
from flask import Flask, url_for, render_template, request, jsonify, json
from flask_session import Session
from bs4 import BeautifulSoup
import re
from werkzeug.utils import redirect

app = Flask(__name__)
# Session(app)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}
# will be an actual DB in the real world
DB = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for(".search", str=request.form.get('search_for'), page=request.form.get('page_num')))
    else:
        return render_template("search.html")


@app.route("/<str>/<page>", methods=["GET", "POST"])
def search(str, page):
    if request.method == "POST":
        return redirect(url_for(".search", str=request.form.get('search_for'), page=request.form.get('page_num')))
    if DB.get(str + 'page' + page):
        return render_template("search.html", results=DB[str + 'page' + page])
    soup = getAmazonPage(str, page)
    if soup.find('title').text == 'Robot Check':
        return render_template("search.html", error="ROBOT CHECK, try again later")
    elif soup.find('title').text == 'Amazon.com Page Not Found':
        return render_template("search.html", error="product not found")
    else:
        q_a = getInfo(soup,str,page)
        return render_template("search.html", results=q_a)


@app.route("/v1/<str>/<page>", methods=["GET", "POST"])
def api(str, page):
    if request.method == "POST":
        return redirect(url_for(".search", str=request.form.get('search_for'), page=request.form.get('page_num')))
    if DB.get(str + 'page' + page):
        return jsonify({"Q_A": DB.get(str + 'page' + page)})
    soup = getAmazonPage(str, page)
    if soup.find('title').text == 'Robot Check':
        return jsonify({'error': "ROBOT CHECK, try again later"})
    elif soup.find('title').text == 'Amazon.com Page Not Found':
        return jsonify({'error': 'product not found'})
    else:
        q_a = getInfo(soup,str,page)
        q_json = json.dumps(q_a)
        return jsonify({"Q_A": q_json})


def getAmazonPage(str, page):
    url = "https://www.amazon.com/ask/questions/asin/" + str + '/' + page
    source = requests.get(url, headers=headers)
    return BeautifulSoup(source.text, 'lxml')

def getInfo(soup,str,page):
    dict = {}
    questionContainer = soup.find_all(id=re.compile("^question-"))
    for question in questionContainer:
        key = question.find("span", {"class": "a-declarative"}).text.strip()
        answer = question.parent.find('span', {'class': None})
        if not answer:
            answer = question.parent.find('span', {'class': 'askLongText'})
        if not answer:
            answer = "no answer yet"
        else:
            answer = answer.text.strip()
        dict[key] = answer
        DB[str + 'page' + page] = dict
    return dict
