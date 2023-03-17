def main():
    _ = input()
    heights = [int(_) for _ in input().split()]
    heights.sort()

    print(*heights)


if __name__ == "__main__":
    main()
