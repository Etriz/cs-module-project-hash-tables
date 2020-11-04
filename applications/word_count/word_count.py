def word_count(str_input):
    # Your code here
    word_dict = dict()

    # need r string to ignore backslash functionality in blacklist
    blacklist = set(r'":;,.-+=/\|[]{}()*^&')
    clean = "".join(char for char in str_input if char not in blacklist)
    if clean == "":
        return word_dict

    words = clean.lower().split()
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )
