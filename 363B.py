def main():
    n, k = (int(_) for _ in input().split())
    heights = [int(_) for _ in input().split()]
    acc = [0 for _ in range(len(heights) + 1)]

    for i in range(len(heights)):
        acc[i + 1] = acc[i] + heights[i]

    min_sum = 1e9
    min_index = -1

    for i in range(k, len(acc)):
        if acc[i] - acc[i - k] < min_sum:
            min_sum = acc[i] - acc[i - k]
            min_index = i

    print(min_index - k + 1)


if __name__ == "__main__":
    main()
