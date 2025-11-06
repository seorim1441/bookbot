from stats import get_words_numbers
from stats import get_char_numbers
from stats import sorted_list
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()

	return file_contents

def main():
    if len(sys.argv) != 2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit(1)
          return
    else:
          path_to_book = sys.argv[1]
    number_of_words = get_words_numbers(get_book_text(path_to_book))

    a = sorted_list(get_char_numbers(get_book_text(path_to_book)))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    
    for b in a:
        print(f"{b["char"]}: {b["num"]}")

    print("============= END ===============")
    # print(sys.argv)
main()