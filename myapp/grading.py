from .helperfunct import *
from .score_to_grade import *
import re
import math
# from nltk.tokenize import sent_tokenize

def grading(text):

    words = text.split()

    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    syllable_count = 0

    for word in words:
        syllable_count += count_syllables(word)

    average_sentence_length = word_count / sentence_count 
    average_syllables_per_word = syllable_count / word_count
    
    # Calculate Flesch Reading Ease (FRE) score
    fre = freGrade(round((206.835 - (1.015 * average_sentence_length) - (84.6 * average_syllables_per_word)), 3))
    
    # Calculate Flesch-Kincaid Grade Level (FKRA) score
    fkra = fkraANDcliANDsmogGrade(round(((0.39 * average_sentence_length) + (11.8 * average_syllables_per_word) - 15.59), 3))

    # Calculate the Coleman-Liau Index
    total_letters = len(re.findall(r'\w', text))
    average_letters = (total_letters / word_count) * 100
    average_sentences = (sentence_count / word_count) * 100
    cli = fkraANDcliANDsmogGrade(round((0.0588 * average_letters - 0.296 * average_sentences - 15.8), 3))

    # Count the total number of polysyllabic words and sentences
    polysyllabic_word_count = count_polysyllabic_words(text)
    smog = fkraANDcliANDsmogGrade(round((1.0430 * math.sqrt(polysyllabic_word_count * 30 / sentence_count) + 3.1291), 3))

    #Calculate the Automated Readability Index
    ari = ariGrade(round((4.71 * (average_letters / 100) + 0.5 * average_sentence_length - 21.43), 3))

    return word_count, fre, fkra, cli, smog, ari