def tanya_substraction(n):
    if n % 10 == 0:
        n /= 10
    else:
        n -= 1
    return int(n)

def main():
    n, k = (int(_) for _ in input().split())

    for _ in range(k):
        n = tanya_substraction(n)

    print(n)


if __name__ == "__main__":
    main()
