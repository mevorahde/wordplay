import pytest
from wordplay import score_word, lexicon_file, word_list


@pytest.mark.parametrize("word, score", [
    ("", 0),
    ("a", 1),
    ("bird", 7),
    ("cat", 5),
    ("fish", 10),
    ("bliffy", 17),
])
def test_score_word(word, score):
    assert score_word(word) == score


def test_word_list_lower():
    loop_list = word_list(lexicon_file("sowpods.txt"))
    for word in loop_list:
        assert word.islower()


def test_word_list_hash():
    loop_list = word_list(lexicon_file("sowpods.txt"))
    for word in loop_list:
        assert word != "#"


def test_word_list_blank_line():
    loop_list = word_list(lexicon_file("sowpods.txt"))
    for word in loop_list:
        assert word != " "