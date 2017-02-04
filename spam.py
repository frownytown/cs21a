# -----------------------------------------------------------------------------
# Name:        spam.py
# Purpose:     This program will classify messages as either spam or not spam
#               Discarding those that appear to spam
#
# Author:   Roger McClain
# Date: 2/3/2017
# -----------------------------------------------------------------------------
"""
This code compares the content of a message with a list of known spam words.

Using the list of known spam words this code compares the content of a message
input by the user to determine the ratio of content that is common spam words.
if the ratio is above 0.10 the code concludes that the message is spam.
"""
import string
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}

SPAM_THRESHOLD = 0.10

def spam_indicator(text):
    """
    This function transforms input into a list and compares it to spam word list
    and returns the ratio of spam words to non spam words.
    """
    # This function returns the spam indicator rounded to two decimals

    word_list = text.split()        # Turning string into list
    unique_words = set(word_list)   # Turning list into set
    shared_words = unique_words & SPAM_WORDS    # Intersection of two sets
    shared_ratio = (len(shared_words)) / (len(unique_words))   # Finding ratio
    rounded_ratio = round(shared_ratio, 2)      # Rounding ratio to two places
    return rounded_ratio        # Return rounded ratio
def classify(indicator):
    """
    This function prints whether or not the message is spam.
    """
    # This function prints the spam classification
    if indicator > SPAM_THRESHOLD:  # If ratio above 0.10 then SPAM
        print('Spam indicator: ' + str(indicator))
        print('This message is: SPAM')
    else:                           # If ratio anything else then HAM
        print('Spam indicator: ' + str(indicator))
        print('This message is: HAM')

def get_input():
    """
    This is the funtion that prompts the user for input, it also excludes
    punctuation and converts everything to lowercase.
    """
    # Prompt the user for input and return the input
    while True:
        user_input = input('Please enter your message: ')   # Prompt for input
        lower_input = user_input.lower()             # Convert to lowercase
        # Creates a set of punctuation in order to exclude them from our code
        exclude_chars = set(string.punctuation)
        fixed_input = ''.join(ch for ch in lower_input if ch not in
                              exclude_chars)    # Remove punctuation
        return fixed_input      # Return input that is cleaned up
def main():
    # Get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator
    # Call classify to print the classification
    lower_input = get_input()   # Var lower_input is what get_input() returns
    final_ratio = spam_indicator(lower_input)   # Pass lower_input into spam
    classify(final_ratio)   # Pass the rounded ratio into classify and print

if __name__ == '__main__':
    main()      # Call main function
