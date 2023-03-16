def main():
    n = int(input())
    
    count = 0

    for _ in range(n):
        p, q = (int(_) for _ in input().split())
        if q - p >= 2:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
