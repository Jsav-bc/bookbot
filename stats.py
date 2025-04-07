from sys import argv
def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    
    return content

def get_word_count():
    content = get_book_text(argv[1])
    w_c = 0
    w_list = content.split()
    for w in w_list:
        w_c += 1

    return w_c

def get_char_count():
    char_d = {}
    c_c = 0
    content = get_book_text(argv[1])
    content = content.lower()

    for c in content:
        if c not in char_d:
            char_d[c] = 1
        else:
            char_d[c] += 1
    
    return char_d

def report_struct(char_d):
    return {k: v for k, v in sorted(char_d.items(), key=lambda item: item[1],reverse=True)}

def report():
    ww = get_word_count()
    wc = get_char_count()
    cc = report_struct(wc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {ww} total words")
    print("--------- Character Count -------")
    for c in cc:
        if c.isalpha():
            print(f"{c}: {cc[c]}")
        else:
            pass
    print("============= END ===============")
