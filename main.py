def count_letters(words):
    counter = {}
    for word in words:
        for char in word.lower():
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

    return counter

def print_report(num_words, sorted_desc_lst):
    # print(sorted_desc_lst)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{num_words} words found in the document")
    print()
    for character, count in sorted_desc_lst:
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")
    print('--- End report ---')

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    counter = count_letters(words)
    # print(counter)
    dict_lst_version = sorted(list(counter.items()), key=lambda item:item[1], reverse=True)
    print_report(num_words, dict_lst_version)


