def main():
    word = input()

    upper = 0
    lower = 0

    for char in word:
        if char.isupper():
            upper += 1
        else:
            lower += 1

    if lower >= upper:
        print(word.lower())
    else:
        print(word.upper())


if __name__ == "__main__":
    main()
