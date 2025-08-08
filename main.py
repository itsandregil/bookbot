import sys

from stats import count_characters, get_num_words, get_sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Get second argument of sys.argv
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counts = count_characters(text)
    sorted_counts = get_sorted_chars(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_counts:
        print(f"{count['char']}: {count['num']}")
    print("============= END ===============")


main()
