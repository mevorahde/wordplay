#!/usr/bin/env python3

from flask import Flask, jsonify, request
import wordplay


app = Flask(__name__)


@app.route("/")
def hello():
    return """<h1>Flask is running!</h1>
    <p>Try accessing the <a href="/api/v1/data">dummy data</a> endpoint.</p>
    <p>Score letters <a href="/api/v1/score?l=wombat">'wombat'</a></p>
    """


@app.route("/api/v1/data")
def dummy_data():
    data = {'message': 'looks like it works!',
            'values': list(range(9))}
    return jsonify(data)


@app.route("/api/v1/score")
def score_word():
    letters = request.args.get('l')
    score = wordplay.score_word(letters)
    result = {'letters': sorted(list(letters)),
              'score': score}
    return jsonify(result)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
