def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    
    return content

def get_word_count():
    content = get_book_text("books/frankenstein.txt")
    w_c = 0
    w_list = content.split()
    for w in w_list:
        w_c += 1

    return w_c

def get_char_count():
    char_d = {}
    c_c = 0
    content = get_book_text("books/frankenstein.txt")
    content = content.lower()

    for c in content:
        if c not in char_d:
            char_d[c] = 1
        else:
            char_d[c] += 1
    
    char_d.sort(key=c, reverse = True)
    return char_d

def report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count()} total words")
    print("--------- Character Count -------")
    sort