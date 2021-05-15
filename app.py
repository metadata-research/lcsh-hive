from flask import Flask, jsonify, render_template

import requests


app = Flask(__name__)

@app.route('/')
def index():
    return '<html>Welcome to the 1910 Library of Congress Subject Headings. Presented by HIVE2 start <a href = "/99152/b47p8tc5z">here</a> </html>'

@app.route('/99152/<ark>')
def get_term(ark):
    hive_uri = 'https://hive2.cci.drexel.edu/getConceptInfo?id={}&voc=lcsh1910'.format(ark)
    hive_response = requests.get(hive_uri,verify=False).json()

    return render_template('term.html', data = hive_response)



if __name__ == "__main__":
    app.run()