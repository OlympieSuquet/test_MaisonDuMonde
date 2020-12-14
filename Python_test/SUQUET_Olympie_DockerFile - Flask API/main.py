from flask import Flask, jsonify

import SparseArray
import sys
import os

app = Flask(__name__)

@app.route('/')
def main():
    strings = os.getenv('STRINGS').split(',')
    queries = app.config.get('queries').split(',')
    x = SparseArray.SparseArray(queries,strings)
    print(x.matchingStrings())
    return x.matchingStrings()

if __name__ == '__main__':
    app.config['queries'] = sys.argv[1]
    app.run(debug=True, host='0.0.0.0')
