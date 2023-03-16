def main():
    _ = input()
    proportions = [int(_) for _ in input().split()]

    print(sum(proportions) / len(proportions))


if __name__ == "__main__":
    main()
