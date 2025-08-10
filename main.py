import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

# Function to return the contents of the file whose name is passed
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    contents = get_book_text(filepath) 
    num_words = get_num_words(contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    num_chars = get_num_chars(contents)
    sorted_chars = get_sorted_num_chars(num_chars)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(item["char"], ":", sep="", end=" ")
            print(item["num"])

    print("============= END ===============")

main()