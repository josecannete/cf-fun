def main():
    n = int(input())

    for _ in range(n):
        word = input()
        output = []
        for i in range(len(word)):
            if word[i] != "0":
                rn = word[i] + "0" * (len(word) - i - 1)
                output.append(rn)
        print(len(output))
        print(*output)


if __name__ == "__main__":
    main()
