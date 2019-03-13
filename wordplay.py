#!/usr/bin/env python3
import io

scrabble_point_values = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                         "x": 8, "z": 10}


def score_word(word: str) -> int:
    score = 0
    for letter in word:
        score += scrabble_point_values[letter]
    return score


# print(score_word("word"))


def lexicon_file(filename: str)-> list:
    with open(filename) as lexicon_file:
        return read_words(lexicon_file)


# this method we can test by passing in a `io.StringIO` substitute
def read_words(file_obj: str) -> list:
    word_list = []
    # for line in read_lines:
    for line in (file_obj.readlines()):
        line =  line.strip()
        if not line.startswith("#") and line:
            word_list.append(line.lower())
    print(word_list)
    # print(len(word_list))
    return word_list
    input_file.close()


lexicon_file("sowpods.txt")

