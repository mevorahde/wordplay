import pytest, io
from wordplay import score_word, read_words


@pytest.mark.parametrize("word, score", [
    ('', 0),
    ('a', 1),
    ('bird', 7),
    ('cat', 5),
    ('fish', 10),
    ('bliffy', 17),
    ('xylophone', 24),
    ('leet-speak', 15),
    ('l33t-sp34k', 11),
])
def test_score_word(word, score):
    assert score_word(word) == score


# a random sample of words from sowpods.txt
LEXICON_CONTENTS = """
COMPRISABLE
HOSES
HUSKLIKE
MOTUCAS
PHANEROPHYTE
PLAINCHANTS
POWDER
QUANTA
TACTUALITIES
WHIPPETS
""".strip()

EXPECTED_WORDS = [line.strip().lower() for line in LEXICON_CONTENTS.split()]


def test_read_words_empty_file():
    file_contents = io.StringIO('')
    words = read_words(file_contents)
    assert words == []


def test_read_words_normal():
    file_contents = io.StringIO(LEXICON_CONTENTS)
    words = read_words(file_contents)
    assert words == EXPECTED_WORDS


def test_read_words_skip_empty_lines_and_comments():
    contents = LEXICON_CONTENTS.replace('\n','\n\n# some comment about a word\n')
    print("lexicon contents:", contents, sep='\n')
    file_contents = io.StringIO(contents)
    words = read_words(file_contents)
    assert words == EXPECTED_WORDS
