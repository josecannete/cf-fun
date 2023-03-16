def check_completed(arr):
    for i in arr:
        if i is False:
            return False
    return True


def main():
    n = int(input())
    x_levels = list(int(_) for _ in input().split())
    y_levels = list(int(_) for _ in input().split())

    completed = [False for _ in range(n)]

    for i in range(1, len(x_levels)):
        completed[x_levels[i] - 1] = True

    for i in range(1, len(y_levels)):
        completed[y_levels[i] - 1] = True

    if check_completed(completed):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")


if __name__ == "__main__":
    main()
