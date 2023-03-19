def main():
    a, b = (int(_) for _ in input().split())

    count = a

    while a / b >= 1:
        count += int(a / b)
        a = int(a / b) + a % b

    print(count)


if __name__ == "__main__":
    main()
