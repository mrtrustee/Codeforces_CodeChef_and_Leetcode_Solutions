import string
def is_pangram(st):
    Convert = [a.lower() for a in st if a.isalpha()]
    return set(Convert) >= set(string.ascii_lowercase)