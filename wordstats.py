# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:
#
# Author:   Roger McClain
# Date: 2/8/2017
# -----------------------------------------------------------------------------
"""
Retrieve some statistics about a very long text file

This program will accept a text file and print out one of the longest words as
well as a list of the most common words. It will also write to a file in the
cwd called 'out.txt' with a dictionary of all the words in the text and the
number of times they appear in the text. It will also generate a word cloud.
"""

# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random
import string

# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


# Enter your own helper function definitions here
def five_most_common(unsorted_dict):
    """
    Sorts the dictionary by transforming it into a list of tuples

    Parameter: Dictionary returned from count_words()
    Return: Sliced list of tuples representing five most common words
    """
    # sorting dictionary by the values, reversing it so the most common at top
    sorter = sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_again = sorter[0:5]  # slice to get only top 5
    return sorted_again

def longest_word(unsorted_dict):
    """
    Find one of the longest words in the text and return it so that it can
    be printed
    """
    # returns one of the longest words, maybe unnecessary function, not sure
    # how to better organize it though
    return max(unsorted_dict, key=len)


def count_words(filename):
    """
    Get the words from a file

    Parameters: THe name of a file
    Return: A dictionary containing words and their number of occurrences
    """
    # build and return the dictionary for the given filename
    word_dictionary = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower() # make everything lowercase
            for word in line.split():   # break string into list
                # remove all the punctuation
                word = word.strip(string.punctuation + string.digits)
                if word:
                    if word not in word_dictionary.keys():
                        word_dictionary[word] = 1
                    else:
                        word_dictionary[word] += 1
        return word_dictionary



def report(word_dict):
    """
    Write to a output file reporting statistics about input file

    Parameters: Raw data
    Return: Writes to a text file with the list of all words and appearance #
    """
    # report on various statistics based on the given word count dictionary
    with open('out.txt', 'w', encoding='utf-8') as file:
        for k, v in sorted(word_dict.items()):
            print(k, ': ', v, file=file)
        return


def main():
# get the input filename and save it in a variable
# call count_words to build the dictionary for the given file
# save the dictionary in the variable word_count
# call report to report on the contents of the dictionary word_count
    ref_name = input('Please enter the reference file name: ')
    unsorted_dict = count_words(ref_name)  # get the reference words

    post_sort = five_most_common(unsorted_dict)
    report(unsorted_dict)   # writing to output file
    draw_cloud(unsorted_dict, 3) # changed word cloud to start with len 3
    print('The longest word is: ' + longest_word(unsorted_dict))
    print('The 5 most common words are:')
    for x in post_sort:
        print("%s: %s"% x)  # formatting for the print







# If you want to generate a word cloud, uncomment the line below.
#draw_cloud(word_count)


if __name__ == '__main__':
    main()