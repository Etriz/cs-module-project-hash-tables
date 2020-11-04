def no_dups(s):
    # Your code here
    word_dict = dict()
    word_list = s.split()

    for w in word_list:
        if w not in word_dict:
            word_dict[w] = True

    word_dict = " ".join(word_dict)

    return word_dict

    # this doesn't work because sets are unordered
    # return " ".join(set(s.split()))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
