from stats import word_count
from stats import char_count
from stats import sort_char
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")


    frank = get_book_text(book_path)
    text = word_count(frank)
    count = len(text)
    char_list = []

    char_dict = char_count(frank)

    for char, count2 in char_dict.items():
        char_list.append({"char": char, "num": count2})


    char_list.sort(reverse=True, key=sort_char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in char_list:
        char = item["char"]

        if not char.isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")



main()