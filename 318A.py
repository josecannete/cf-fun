def main():
    n, k = (int(_) for _ in input().split())

    if n % 2 == 1:
        n += 1

    if k > n / 2:
        print(int(2 * (k - (n / 2))))
    else:
        print((2 * k) - 1)


if __name__ == "__main__":
    main()
