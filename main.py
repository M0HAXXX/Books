# https://teasd.chsv-marasa-sha.repl.co/books - ссылка

from flask import Flask, request
import requests
from db import RESULTS

app = Flask('Library')


@app.route('/books', methods=['GET'])
def START():
    return {'Output': RESULTS}


@app.route('/books', methods=['POST'])
def LAST():
    books_start = request.form['books_start']
    
    RESULTS.append({'book': books_start})

    return {'Output': RESULTS}


app.run(host = '0.0.0.0', port = 3000)

