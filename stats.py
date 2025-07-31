def get_word_count(contents):
    word_list = contents.split()
    return len(word_list)

def get_letter_count(contents):
    letters = {}
    for letter in contents.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters