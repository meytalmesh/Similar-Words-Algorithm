import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

dictionary = None
num_words = 0


class WordNotFound(Exception):
    pass


def _sort_chars(word: str) -> str:
    return "".join(sorted(word))


def init_dictionary() -> dict:
    global dictionary, num_words

    try:
        with open("words_clean.txt", "r") as file:
            # Assuming each line in the text file represents a word
            dictionary = defaultdict(set)
            for word in file:
                stripped_word = word.strip()
                dictionary[_sort_chars(stripped_word)].add(stripped_word)
                num_words += 1
    except FileNotFoundError:
        logger.error("'words_clean.txt' not found.")
    return dictionary


def get_similar_words(word: str) -> list[str]:
    global dictionary

    if dictionary is None:
        dictionary = init_dictionary()

    key = _sort_chars(word)
    if key not in dictionary:
        raise WordNotFound(f"Word '{word}' not found")

    if word not in dictionary[key]:
        raise WordNotFound(f"Word '{word}' not found")

    return [w for w in dictionary[key] if w != word]


def get_total_words() -> int:
    global num_words
    return num_words