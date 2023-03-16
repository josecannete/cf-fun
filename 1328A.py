def main():
    n = int(input())

    for _ in range(n):
        a, b = (int(_) for _ in input().split())
        print((b - a % b) % b)


if __name__ == "__main__":
    main()
