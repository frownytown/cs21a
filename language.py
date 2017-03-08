# -----------------------------------------------------------------------------
# Name:        language
# Purpose:  This program will generate infinite random sentences based on a
#           text file
#
# Author:   Roger McClain
# Date: 3/1/2017
# -----------------------------------------------------------------------------
"""
This is a module that learns which words follow other words and then creates
new sentences based on the word ordering that it has learned.

"""
import random
import string
# Enter your imports here


def learn(filename):
    """
    Open file and learn the words and structure

    Parameters:
    This function takes a text file as its parameter.

    Return:
    Returns a Tuple containing the first word of the file, and a dictionary of
    words as the keys, and the follower words as the values.
    """
    words = {}  # Create empty dictionary
    first = None    # Initialize first variable
    previous_word = None
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            text_split = []
            for word in line.split():
                processed_word = word.strip(string.punctuation)
                processed_word = processed_word.lower()
                if len(processed_word) > 0:
                    text_split.append(processed_word)
                    if first is None:
                        # Get the first word in the text file
                        first = text_split[0]
            # iterate over text and create dict of words and followers
            if previous_word:
                text_split.insert(0, previous_word)
            for counter, word in enumerate(text_split):
                if word not in words:
                    words[word] = []
                if counter < (len(text_split) - 1):
                    words[word].append(text_split[counter + 1])
            previous_word = text_split[-1]
        return first, words     # return a tuple of first word and dict


def sentence_generator(filename, length=10):
    """
    Makes up random sentences based on the words dictionary, chooses a random
    word from a words followers until it hits the inputted length.

    Parameter:
    This function can take a text file (or the result of the Learn function) as
    its first parameter, and it takes a sentence length as its second parameter
    with the default length being 10.
    """
    random.seed(1)  # Set the seed for the random generator - do not remove
    # Enter your code here
    learned_tuple = learn(filename)
    sorted_words = sorted(learned_tuple[1])     # Sort the dictionary
    current_word = random.choice(sorted_words)   # Randomly select first word
    sentence_data = [current_word]  # create list
    sentence_length = len(sentence_data)    # Create length to compare too
    while True:  # infinite loop for Generator Function
        current_word = sentence_data[-1]    # Word to start with
        next_word = determine_next_word(learned_tuple[1][current_word],
                                        learned_tuple[0])
        # Logic to create the sentence by appending random words
        sentence_data.append(next_word)
        sentence_length += 1    # Insuring the proper number of loops
        # So that we only loop proper number of times
        if len(sentence_data) == length:
            temp_var = ' '.join(sentence_data)
            sentence_data = [random.choice(sorted_words)]
            yield temp_var      # Yield so that function can be resumed


def determine_next_word(possible_options, default):
    """
    This is a function that determines the next word that the sentence
    generator uses.

    Parameter:
    Takes the values from the Learn function as its first parameter, and the
    second parameter is the first word of the text file.

    Return:
    Either returns the first word in the text file if there are no follower
    word option, or it returns a random choice from the follower word list.
    """

    if len(possible_options) == 0:
        return default
    return random.choice(possible_options)

