def is_nearly_lucky(word):
    count = 0
    for char in word:
        if is_lucky(char):
            count += 1
    return is_lucky(str(count))


def is_lucky(word):
    for char in word:
        if char != "4" and char != "7":
            return False
    return True


def main():
    word = input()
    if is_nearly_lucky(word):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
