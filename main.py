def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_chars_dict(text)
    print_report(char_dict, word_count)

def print_report(char_dict, word_count):
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words foun in the document")

    print()
    for char in sorted_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict[char]} times")

    print("--- End report ---")

def get_chars_dict(text):
    chars = {}

    for char in text:
        lowered_char= char.lower()
        if lowered_char in chars.keys():
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1

    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()

    return len(words)


main() 