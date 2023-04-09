def adjacent_borders(n, m, x, y):

    d_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    num_borders = 0

    for dx, dy in d_pos:
        if x + dx > n or x + dx < 1:
            num_borders += 1
        if y + dy > m or y + dy < 1:
            num_borders += 1

    return num_borders


def main():
    t = int(input())
    for _ in range(t):
        n, m = (int(_) for _ in input().split())
        x1, y1, x2, y2 = (int(_) for _ in input().split())

        adj1 = 4 - adjacent_borders(n, m, x1, y1)
        adj2 = 4 - adjacent_borders(n, m, x2, y2)

        # print(f'{x1} {y1} {adj1}')
        # print(f'{x2} {y2} {adj2}')

        min_obs = min(adj1, adj2)
        print(min_obs)


if __name__ == "__main__":
    main()
