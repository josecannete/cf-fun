def main():
    s, n = (int(_) for _ in input().split())

    dragons = []

    for _ in range(n):
        sd, rd = (int(_) for _ in input().split())
        dragons.append((sd, rd))

    dragons.sort(key=lambda x: x[0])

    acc_str = s

    for dragon in dragons:
        if acc_str > dragon[0]:
            acc_str += dragon[1]
        else:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
