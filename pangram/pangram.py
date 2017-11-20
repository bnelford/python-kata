import string

def is_pangram(phrase):
    alphabet = string.ascii_lowercase
    lowerphrase = phrase.lower()
    for letter in alphabet:
        if lowerphrase.find(letter)==-1:
            return False
    return True
