# -----------------------------------------------------------------------------
# Name:        spam.py
# Purpose:     This program will classify messages as either spam or not spam
#               Discarding those that appear to spam
#
# Author:   Roger McClain
# Date: 2/3/2017
# -----------------------------------------------------------------------------
"""
Enter your module docstring with a one-line overview here

and a more detailed description here.
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
    Enter your function docstring here
    """
    # This function returns the spam indicator rounded to two decimals

    word_list = text.split()
    unique_words = set(word_list)
    shared_words = unique_words & SPAM_WORDS
    shared_ratio = (len(shared_words)) / (len(unique_words))
    rounded_ratio = round(shared_ratio, 2)
    return rounded_ratio
def classify(indicator):
    """
    Enter your function docstring here
    """
    # This function prints the spam classification
    if indicator > SPAM_THRESHOLD:
        print('Spam indicator: ' + str(indicator))
        print('This message is: SPAM')
    else:
        print('Spam indicator: ' + str(indicator))
        print('This message is: HAM')

def get_input():
    """
    Enter your function docstring here
    """
    # Prompt the user for input and return the input
    while True:
        user_input = input('Please enter your message: ')
        lower_input = user_input.lower()
        exclude_chars = set(string.punctuation)
        fixed_input = ''.join(ch for ch in lower_input if ch not in
                              exclude_chars)    # remove punctuation
        return fixed_input
def main():
    # Get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator
    # Call classify to print the classification
    lower_input = get_input()
    final_ratio = spam_indicator(lower_input)
    classify(final_ratio)

if __name__ == '__main__':
    main()
