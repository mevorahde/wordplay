#!/usr/bin/env python3
from flask import Flask, jsonify, request
import wordplay


app = Flask(__name__)


@app.route("/")
def hello():
    return """<form action="/api/v1/score?l=<word>" method="post">
    <p>Please enter a word: </p>
    <input type="text" name="word">
    <input type="submit">
    </form>
    <p>Try accessing the <a href="/api/v1/data">dummy data</a> endpoint.</p>
    <p>Score letters <a href="/api/v1/score?l=wombat">'wombat'</a></p>
    """

@app.route("/api/v1/data")
def dummy_data():
    data = {'message': 'looks like it works!',
            'values': list(range(9))}
    return jsonify(data)


@app.route("/api/v1/score", methods=['POST'])
def score_word():
    word = request.form['word']
    lowercase_word = word.lower()
    word_list = wordplay.word_list
    if lowercase_word in word_list:
        score = wordplay.score_word(lowercase_word)
        result = {'letters': sorted(list(lowercase_word)),'score': score}
    else:
        result = "You did not enter a valid word."
    return jsonify(result)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
