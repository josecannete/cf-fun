def main():
    word = input()

    if word.isupper():
        print(word.lower())
    elif word[0].islower():
        if len(word) == 1:
            print(word.upper())
        elif len(word) > 1 and word[1:].isupper():
            print(word[0].upper() + word[1:].lower())
        else:
            print(word)
    else:
        print(word)


if __name__ == "__main__":
    main()
