def main():
    t = int(input())

    directions = {"DR": (1, 1), "DL": (1, -1), "UR": (-1, 1), "UL": (-1, -1)}
    inverse_directions = {(1, 1): 0, (1, -1): 1, (-1, 1): 2, (-1, -1): 3}

    for _ in range(t):
        n, m, i1, j1, i2, j2, d = input().split()
        n, m, i1, j1, i2, j2 = (int(_) for _ in (n, m, i1, j1, i2, j2))
        d = directions[d]

        visited = [
            [[False for _ in range(4)] for _ in range(m + 1)] for _ in range(n + 1)
        ]

        # print(visited)
        # print(len(visited[0][0]))

        current_i, current_j = i1, j1
        bounces = 0
        reached = False

        while not visited[current_i][current_j][inverse_directions[d]]:
            # print(current_i, current_j)
            visited[current_i][current_j][inverse_directions[d]] = True

            if current_i == i2 and current_j == j2:
                print(bounces)
                reached = True
                break
            else:
                add_bounces = 0
                if current_i + d[0] == n + 1 or current_i + d[0] == 0:
                    # print("bounce i")
                    d = (d[0] * -1, d[1])
                    add_bounces += 1
                if current_j + d[1] == m + 1 or current_j + d[1] == 0:
                    # print("bounce j")
                    d = (d[0], d[1] * -1)
                    add_bounces += 1
                if add_bounces >= 1:
                    bounces += 1

                current_i += d[0]
                current_j += d[1]

        if not reached:
            print(-1)


if __name__ == "__main__":
    main()
