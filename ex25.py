def break_words(stuff):
    """This function will break words for us"""
    words = stuff.split()
    return words

def sort_words(words):
    """This function will sord the words"""
    return sorted(words)

def print_first_word(words):
    """This function will print the first word after popping it off"""
    word = words.pop(0)
    return word

def print_last_word(words):
    """This function will print the last word after popping it off"""
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This function takes a sentence and print the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
