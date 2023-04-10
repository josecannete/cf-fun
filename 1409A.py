def main():
    t = int(input())

    for _ in range(t):
        a, b = (int(_) for _ in input().split())
        diff = abs(a - b)

        steps = diff / 10
        if diff % 10 != 0:
            steps += 1

        print(int(steps))


if __name__ == "__main__":
    main()
