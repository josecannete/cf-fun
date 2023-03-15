def reverse_word(word):
    reverse = ""
    for i in range(len(word)):
        reverse += word[len(word) - 1 - i]
    return reverse


def main():
    ber_word = input()
    bir_word = input()

    if reverse_word(ber_word) == bir_word:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
