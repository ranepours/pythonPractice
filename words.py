def print_caps(words):
    """print each word on a separate line in caps"""
    for word in words:
        print(word.upper())

def print_caps_e(words):
    """print each word on a separate in line in caps only starting with the letter 'e' """
    for word in words:
        if word.startswith('E') or word.startswith('e'):
            print(word.upper())

def print_specified_caps(words, start):
    """pass in a set of letters and only those words are printed in caps in separate lines"""
    for word in words:
        for letter in start:
            if word.startswith(letter):
                print(word.upper())
