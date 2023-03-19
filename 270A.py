def main():
    n = int(input())

    regular_polygon = [180 * (i - 2) / i for i in range(3, 1000)]

    for _ in range(n):
        angle = int(input())
        if angle in regular_polygon:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
