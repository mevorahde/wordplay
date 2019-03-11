#!/usr/bin/env python3

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

def lexicon_file(filename: str)->list:
    input_file = open(filename, "r")
    read_lines = input_file.readlines()
    word_list = []
    for line in read_lines:
        if not line.strip() or not line.startswith("#"):
            lower_word = line.lower()
            word_list.append(lower_word.strip())
    # print(word_list)
    # print(len(word_list))
    return word_list
    input_file.close()


lexicon_file("sowpods.txt")


def word_list(passed_list: list)-> list:
    return passed_list


word_list(lexicon_file("sowpods.txt"))


