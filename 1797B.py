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
        n, k = (int(_) for _ in input().split())
        matrix = []
        for _ in range(n):
            row = [int(_) for _ in input().split()]
            matrix.append(row)

        rotated = []
        for i in range(len(matrix)):
            rotated.append(matrix[len(matrix) - i - 1].copy())
            rotated[i].reverse()

        different = 0

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != rotated[i][j]:
                    different += 1

        different /= 2

        if different > k:
            print("NO")
        else:
            if len(matrix) % 2 == 1:
                print("YES")
            elif (different - k) % 2 == 0:
                print("YES")
            else:
                print("NO")

        # x = 2, y = 1
        # print(matrix[1][2])


if __name__ == "__main__":
    main()
