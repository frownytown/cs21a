# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:   Roger McClain
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys
# Enter your function definitions here


def scrape_url(url):
    """
    Opens the url and decodes it as well as handling errors.

    :param url:
    :return: Returns the decoded text from the webpage.
    """
    try:
        url_file = urllib.request.urlopen(url)  # Open Url
        text = url_file.read().decode('UTF-8')  # Decode web page
    except urllib.error.URLError as url_err:    # Handle error
        print('Error opening url: ', url, url_err)
        return None
    except UnicodeDecodeError as decode_err:    # Handle error
        print('Error decoding url: ', url, decode_err)
        return None
    else:
        return text     # Returns decoded text for use in other function


def topic_references(text, topic):
    """
    Capture references to the given topic found in the given articles outside
    html.
    Parameters:
    text (string) - the input text
    topic (string) - the word we are searching for
    Return:
    all_references (string) - references to the topic found outside html,
                                separated by new line characters.
                                an empty string if there are no such references

    """
    all_references = ''
    # extract text inside angle brackets containing the topic
    pattern = r"\>([^\>]*\b{}\s\b.*?)\<".format(topic)
    matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
    if matches:
        all_references = '\n'.join(matches)
    return all_references


def main():
    if len(sys.argv) != 3:  # Checks command line args
        print('Error: invalid number of arguments')
        print('Usage: aggregator.py filename topic')
        exit()
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as sources:
            for url in sources: # Calls scrape function one url at a time
                url_text = scrape_url(url)
                if url_text is not None:    # Only runs if no error
                    results = topic_references(url_text, sys.argv[2])
                    with open('{}summary.txt'.format(sys.argv[2]), 'a',
                              encoding='utf-8') as append_file:
                        if results:
                            append_file.write('Source: ' + url)
                            append_file.write('\n' + results + '\n')
                            append_file.write('-' * 30 + '\n')
                            # Formatting for output file

if __name__ == '__main__':
    main()
