from stats import get_word_count
from stats import get_letter_count

def get_book_text(filepath):
    with open(filepath) as c:
        file_contents = c.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    word_count = get_word_count(contents)
    letter_dict = get_letter_count(contents)
    print(f"{word_count} words found in the document")
    print(letter_dict)

main()

