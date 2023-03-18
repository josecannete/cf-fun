def main():
    n, m = (int(_) for _ in input().split())

    side = -1
    for i in range(n):
        row = ""
        if i % 2 == 0:
            row = "".join("#" for _ in range(m))
        else:
            row = "".join("." for _ in range(m))
            if side == -1:
                row = row[: m - 1] + "#"
                side = 1
            elif side == 1:
                row = "#" + row[1:m]
                side = -1
        print(row)


if __name__ == "__main__":
    main()
