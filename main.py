from stats import wordcount, analyze, dictsort
import sys

def get_book_text(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    with open(path) as theFile:
        book_text = theFile.read()
    return book_text

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_text = get_book_text(sys.argv[1])

    word_count = wordcount(book_text)
    print(f"Found {word_count} total words")

    d = dictsort(analyze(book_text))
    for i in d:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    return 
    

main()