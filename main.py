# Stores book_path inside variable, text of the book in another using get_book_text.
# Then prints out the text.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_conv_to_sorted_lists(chars_dict)

    print(f"---- Begin report of {book_path} ----")
    print(f"{count_words} found inside the text.")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("---- End of analysis ----")

# This opens a book and reads it from a given path and returns the text.
# For clarification it's used inside the main function and stores the read text inside a variable called text.
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Same as last one, this one takes the a given text and splits it into a list.
# With len() it returns an integer. Then the function gets called inside main and passed the text.
def get_count_words(text):
    words = text.split()
    return len(words)

# Creates an empty dict called chars, then loops through every c (character) in the text,
# using a lower() function to unsure every character is lowercase, the adds 1 if the character is found
# inside the dict. Otherwise it creates a new entry with the value of 1.
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_conv_to_sorted_lists(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()
