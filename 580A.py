def main():
    _ = int(input())

    money = list(int(_) for _ in input().split())

    last_non_dc = 1
    max_non_dc = 1

    for i in range(1, len(money)):
        if money[i] >= money[i - 1]:
            last_non_dc += 1
            max_non_dc = max(last_non_dc, max_non_dc)
        else:
            last_non_dc = 1

    print(max_non_dc)


if __name__ == "__main__":
    main()
