import re

def count_syllables(word):
    # Very basic syllable counting algorithm
    word = word.lower()
    count = 0
    
    if len(word) <= 3:
        return 1
    
    if word.endswith(('es', 'ed')):
        word = word[:-2]
    
    vowels = 'aeiouy'
    current_word = False
    
    for char in word:
        if char in vowels:
            if not current_word:
                count += 1
                current_word = True
        else:
            current_word = False
    
    if word.endswith('e'):
        count -= 1
    
    if count == 0:
        count = 1
    
    return count

def count_complex_words(text):
    # Very basic complex word counting algorithm
    word_list = text.split()
    complex_words = 0
    
    for word in word_list:
        if count_syllables(word) >= 3:
            complex_words += 1
    
    return complex_words

def count_polysyllabic_words(text):
    # Very basic polysyllabic word counting algorithm
    word_list = text.split()
    polysyllabic_words = 0
    
    for word in word_list:
        if count_syllables(word) >= 3:
            polysyllabic_words += 1
    
    return polysyllabic_words
