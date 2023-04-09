def main():
    t = int(input())
    for _ in range(t):
        _ = input()
        x = [int(_) for _ in input().split()]
        x.sort()

        possible = True

        for i in range(1, len(x)):
            if x[i] - x[i - 1] <= 1:
                continue
            else:
                possible = False
                break

        if possible:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
