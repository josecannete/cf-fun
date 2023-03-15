def is_beatiful(word):
    return len(word) == len(set(word))


def main():
    year = input()

    for i in range(int(year) + 1, 10000):
        if is_beatiful(str(i)):
            print(i)
            break


if __name__ == "__main__":
    main()
