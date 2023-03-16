def main():
    word = input()
    word = word.replace("{", "").replace("}", "").split(", ")

    if '' in word:
        word.remove('')

    if not word:
        print(0)
    else:
        print(len(set(word)))


if __name__ == "__main__":
    main()
