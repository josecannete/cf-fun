def main():
    t = int(input())

    for _ in range(t):
        n = input()
        bags = (int(_) for _ in input().split())

        even_acc = 0
        odd_acc = 0

        for bag in bags:
            if bag % 2 == 0:
                even_acc += bag
            else:
                odd_acc += bag

        if even_acc > odd_acc:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
