def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        greater = 2 * n
        lower = 1
        l1 = []
        l2 = []
        for i in range(n):
            if i % 2 == 0:
                l1.append(greater)
                l2.append(lower)
            else:
                l1.append(lower)
                l2.append(greater)
            greater -= 1
            lower += 1

        l2[1] = l2[-1]
        l2[-1] = 2 * n - 1

        print(*l1)
        print(*l2)


if __name__ == "__main__":
    main()
