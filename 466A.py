def main():
    n, m, a, b = (int(_) for _ in input().split())

    if b / m < a:
        if n % m == 0:
            print(int(n / m) * b)
        else:
            opt_one = int(n / m) * b + (n % m) * a
            opt_two = (int(n / m) + 1) * b
            print(min(opt_one, opt_two))
    else:
        print(n * a)


if __name__ == "__main__":
    main()
