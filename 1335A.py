def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        print(n - int(n / 2) - 1)


if __name__ == "__main__":
    main()
