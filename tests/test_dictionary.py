import modules.dictionary
from modules.dictionary import _sort_chars, get_similar_words


def test_sort_chars():
    assert _sort_chars("cat") == "act"


def test_sort_chars_returns_same_key_for_similar_words():
    assert all([
        _sort_chars('aals') == "aals",
        _sort_chars('alas') == "aals",
        _sort_chars('lasa') == "aals",
        _sort_chars('sala') == "aals"
    ])


def test_get_similar_words():
    assert get_similar_words("cat") == ["act"]
    assert get_similar_words("act") == ["cat"]