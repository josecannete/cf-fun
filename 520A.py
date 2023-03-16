def main():
    _ = input()
    word = input()

    word = set(word.lower())

    if len(word) >= 26:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
