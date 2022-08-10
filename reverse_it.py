


word = input("Enter a word: ")


def reverse_word(word):

    split_word = word.split()
    reverse_word = split_word[-1::-1]
    new_word = " ".join(reverse_word)

    print(new_word)


reverse_word(word)


# for i in len(split_word):

#     new_word += i



# print(new_word)