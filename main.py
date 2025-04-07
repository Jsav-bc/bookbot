from stats import get_word_count, get_char_count, report
from sys import argv

def main():
    if len(argv) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    else:
        #print(f"{get_word_count()} words found in the document")
        #print(get_char_count())
        report()


main()