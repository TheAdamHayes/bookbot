
def main():
    book = "books/frankenstein.txt"

    text = get_book(book)
    char_count = get_characters(text)
    sorted_char_count = sort_characters(char_count)

    print(f"{get_words(text)} words were found in the document.")
    
    for letter, amount in sorted_char_count:
        print(f"{letter}: {amount}")


def get_words(text):
    return len(text.split())

def get_book(book):
    with open(book) as book:
        return book.read()

def get_characters(text):
    text = text.lower()
    char_count = {}
    for letter in text:
        if letter.isalpha():
            char_count[letter] = char_count.get(letter, 0) + 1
    return char_count

def sort_characters(char_count):
    return sorted([(key, value) for key, value in char_count.items()], key=lambda item: item[1], reverse=True)

main()