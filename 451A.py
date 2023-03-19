def main():
    n, m = (int(_) for _ in input().split())

    mmin = min(n, m)

    if mmin % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")


if __name__ == "__main__":
    main()
