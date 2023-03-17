def main():
    n = int(input())

    count = 0
    bills = [100, 20, 10, 5, 1]

    for bill in bills:
        count += int(n / bill)
        n = n % bill

    print(count)


if __name__ == "__main__":
    main()
