def main():
    n = int(input())

    for _ in range(n):
        a, b, c = (int(_) for _ in input().split())

        if a - b == c:
            print("-")
        else:
            print("+")


if __name__ == "__main__":
    main()
