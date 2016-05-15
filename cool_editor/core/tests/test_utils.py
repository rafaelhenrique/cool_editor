import re


def count_words(word, sentence):
    """Count the number of occurrences of a word in the sentence"""
    match = re.compile(word)
    return len(match.findall(sentence))
