from stats import get_num_words, number_of_symbols, split_into_char_dict
import sys

def get_book_text(path: str):
    content:str = ""
    with open(path) as f:
        content = f.read()
    return content

def output(num_words, dictlist, bookpath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in dictlist:
        if not pair["char"].isalpha():
            continue
        char = pair["char"]
        num = pair["num"]
        print(f"{char}: {num}")
    

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_num_words(content)
    #print(f"Found {num_words} total words")
    symbols = number_of_symbols(content)
    #print(symbols)
    dictlist = split_into_char_dict(symbols)
    #print(dictlist)
    output(num_words, dictlist, sys.argv[1])
    
main()