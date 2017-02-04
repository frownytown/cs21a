# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     assignment # 3
#
# Author:      Roger McClain
# Date: 1/28/2017
# -----------------------------------------------------------------------------
"""
Translates inputted text to secret language

checks user input for validity, encodes based on the first letter,
"""
import string       # import string stuff to ensure input is valid
user_input = []     # create list
def starts_with_vowel(word):
    """
    This function checks if the first letter of a word starts with a vowel
    """
    # return True if the word starts with a vowel and False otherwise
    #for i in range(0, 1):       #
    if word[0] in ['a','e','i','o','u']:
        return True
    else:
        return False

def encode(user_input):
    """
    Transforms single words in different ways depending on the first letter
    """
    # translate a single word to the secret language
    # call starts_with_vowel to decide which pattern to follow
    # return a single word (translated)
    if starts_with_vowel(user_input):
        vowel_list = user_input
        vowel_list += 'zus'
        return vowel_list
    else:
        const_list = user_input
        const_list += const_list[0]
        const_list = const_list.lstrip(const_list[0])
        const_list += 'ix'
        return const_list


def translate(original_string):
    """
    Translates input by splitting string into list, then creating new list to
    add encoded words to, then joining new_list into a string and returning
    """
    # translate the whole text to the secret language:
    # split the text into a list of words
    # call encode to translate each of the words in the list and build a
    # new list with these translated words
    # join the list of translated words into a single string
    # and return it
    list_of_words = original_string.split()
    new_list = []
    for words in list_of_words:
        new_list.append(encode(words))
    return ' '.join(new_list)

def validate_input(user_input):
    """
    Checks the input to ensure that it is valid, prompts user to try again if
    invalid
    """
    acceptable_characters = string.ascii_lowercase + ' '
    for char in user_input:
        if char not in acceptable_characters:
            print('Invalid input, Try again: ')
            return False
    return True

def get_input():
    """
    This function prompts the user for input until they enter non empty string
    """
    # prompt the user for input repeatedly until they enter a non-empty string
    # return the string entered by the user
    while True:
        user_input = input('Please enter your message: ')
        if user_input != '' and validate_input(user_input):
            return user_input
def main():
    """
    This function ensures the code is run in the proper order
    """
    # get input from the user and save it in a variable
    # translate the saved input by calling translate - save result
    # print the result
    input_valid = get_input()
    final_string = ( translate( input_valid ))
    print('The secret message is: '+ final_string)

if __name__ == '__main__':      # call main function to run the code
    main()


