def main():
    n = int(input())
    
    home_colors = [-1 for _ in range(n)]
    guest_colors = [-1 for _ in range(n)]

    for i in range(n):
        h, g = (int(_) for _ in input().split())
        home_colors[i] = h
        guest_colors[i] = g

    count = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if home_colors[i] == guest_colors[j]:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
