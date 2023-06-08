# FILE NOT NEEDED ANYMORE

from .helperfunct import *
import re
import math

def calculate_flesch_kincaid(text):
    
    words = text.split() # Split the text into words
    
    # Calculate the number of words, sentences, and syllables
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    syllable_count = 0
    
    for word in words:
        syllable_count += count_syllables(word)
    
    # Calculate average sentence length (ASL)
    average_sentence_length = word_count / sentence_count 
    
    # Calculate average syllables per word (ASW)
    average_syllables_per_word = syllable_count / word_count
    
    # Calculate Flesch Reading Ease (FRE) score
    fre = round((206.835 - (1.015 * average_sentence_length) - (84.6 * average_syllables_per_word)), 3)
    
    # Calculate Flesch-Kincaid Grade Level (FKRA) score
    fkra = round(((0.39 * average_sentence_length) + (11.8 * average_syllables_per_word) - 15.59), 3)
    
    return fre, fkra

def calculate_lexile(text):

    words = text.split()

    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    average_sentence_length = word_count / sentence_count 

    lexile = 0.0559 * average_sentence_length - 0.296 * (word_count / sentence_count) - 15.8

def calculate_gunning_fog(text):
    
    sentences = text.split('. ') # Split the text into sentences
    
    # Calculate the total number of words and sentences
    total_words = len(text.split())
    total_sentences = len(sentences)
    
    # Calculate the average words per sentence
    average_words_per_sentence = total_words / total_sentences
    
    # Count the number of complex words (words with 3 or more syllables)
    complex_words = count_complex_words(text)
    
    # Calculate the percentage of complex words
    percentage_complex_words = (complex_words / total_words) * 100
    
    # Calculate the Gunning Fog Index
    fog_index = round((0.4 * (average_words_per_sentence + percentage_complex_words)), 3)
    
    return fog_index

def calculate_coleman_liau(text):
    
    # Count the total number of letters, words, and sentences
    total_letters = len(re.findall(r'\w', text))
    total_words = len(text.split())
    total_sentences = len(re.findall(r'[.!?]', text))
    
    # Calculate the average number of letters per 100 words
    average_letters = (total_letters / total_words) * 100
    
    # Calculate the average number of sentences per 100 words
    average_sentences = (total_sentences / total_words) * 100
    
    # Calculate the Coleman-Liau Index
    coleman_liau_index = round((0.0588 * average_letters - 0.296 * average_sentences - 15.8), 3)
    
    return coleman_liau_index

def calculate_smog(text):
    
    # Count the total number of polysyllabic words and sentences
    polysyllabic_word_count = count_polysyllabic_words(text)
    sentence_count = len(re.findall(r'[.!?]', text))
    
    # Calculate the SMOG grade level
    smog_grade_level = round((1.0430 * math.sqrt(polysyllabic_word_count * 30 / sentence_count) + 3.1291), 3)
    
    return smog_grade_level
