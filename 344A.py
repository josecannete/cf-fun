def main():
    n = int(input())

    shifts = 0
    current_word = ""

    for _ in range(n):
        word = input()
        if current_word != word:
            current_word = word
            shifts += 1

    print(shifts)


if __name__ == "__main__":
    main()
