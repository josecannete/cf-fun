def main():
    word = input()
    word = word.split("WUB")
    word = [w for w in word if w != '']
    print(*word)


if __name__ == "__main__":
    main()
