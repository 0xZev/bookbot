def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lengthText = count_text(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of " + book_path + " ---")
    print(str(lengthText) + " words found in the document\n\n")

    for i in chars_dict:
        print("The " + i +" character was found " + str(chars_dict[i]) + " times.")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_text(book):
    words = book.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

main()