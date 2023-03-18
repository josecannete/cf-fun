def main():
    n = int(input())

    events = list(int(_) for _ in input().split())

    free = 0
    crimes = 0

    for event in events:
        if event == -1:
            if free == 0:
                crimes += 1
            else:
                free -= 1
        else:
            free += event

    print(crimes)


if __name__ == "__main__":
    main()
