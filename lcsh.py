from flask import Flask, render_template

import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ark:/99152/<ark>')
def get_term(ark):
    hive_uri = 'https://hive2.cci.drexel.edu/getConceptInfo?id={}&voc=lcsh1910'.format(
        ark)
    hive_response = requests.get(hive_uri, verify=False).json()

    return render_template('term.html', data=hive_response)


@app.route('/ark:/13183/<ark>/')
def get_survey():
    return "test survey"


@app.route('/webads/')
def survey():
    return render_template('survey.html')


@app.route('/webads/screenshot/')
def screenshot_survey():
    out = []
    with open('data/compare_screenshots.md', 'r') as f:
        data = f.read()
        out = data.split('<br>')

    return render_template('survey_screenshot.html', data=out)


if __name__ == "__main__":
    app.run()
