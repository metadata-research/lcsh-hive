from flask import Flask, render_template

import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ark:/99152/<ark>')
def get_term(ark):
    hive_uri = 'https://hive2.cci.drexel.edu/getConceptInfo?id={}&voc=lcsh1910'.format(ark)
    hive_response = requests.get(hive_uri,verify=False).json()

    return render_template('term.html', data = hive_response)



if __name__ == "__main__":
    app.run()
