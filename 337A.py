def main():
    n, m = (int(_) for _ in input().split())
    pieces = list(int(_) for _ in input().split())
    pieces.sort()

    least_diff = 1e9

    for i in range(n - 1, len(pieces)):
        if least_diff > pieces[i] - pieces[i - n + 1]:
            least_diff = pieces[i] - pieces[i - n + 1]

    print(least_diff)


if __name__ == "__main__":
    main()
