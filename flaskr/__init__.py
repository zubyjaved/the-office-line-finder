from flask import Flask, render_template, request
import json
from fuzzywuzzy import fuzz
import textwrap

def create_app(test_config=None):
    # creates & configures app
    app = Flask(__name__, instance_relative_config=True)
    
    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/results', methods=['POST'])
    def results():
        text = request.form['inputTxt']
        response = get_best_line(text)
        output = "<br>INPUT : " + text + "<br>CLOSEST MATCH : " + response['line_text']
        output += "<br>SPEAKER : " + response['speaker'] + '<br>SEASON : ' + str(response['season']) + '<br>EPISODE : ' + str(response['episode'])
        return output

    return app

def get_best_line(text):
    with open('flaskr/static/office-script.json') as f:
        data = json.load(f)
        bestLine = data[0]
        bestRatio = fuzz.ratio(text, bestLine['line_text'])

        for line in data:
            theLine = str(line['line_text'])
            ratio = fuzz.ratio(text, theLine)

            if ratio > bestRatio:
                bestLine = line
                bestRatio = ratio

        return bestLine