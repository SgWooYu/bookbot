def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    letters = count_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count(text):
    words = text.split()
    return len(words)


def count_letters(text):
    dict = {}
    for t in text:
        lcase = t.lower()
        if lcase in dict:
            dict[lcase] += 1
        else:
            dict[lcase] = 1
    return dict


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()