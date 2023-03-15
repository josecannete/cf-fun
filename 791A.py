def main():
    a, b = (int(_) for _ in input().split())
    years = 0
    while a <= b:
        years += 1
        a *= 3
        b *= 2
    print(years)


if __name__ == "__main__":
    main()
