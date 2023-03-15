def main():
    a = int(input())
    steps = int(a / 5)
    if a % 5 != 0:
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
