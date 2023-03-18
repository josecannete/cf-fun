def main():
    a = int(input())
    b = int(input())
    c = int(input())

    one = a + b + c
    two = a + b * c
    twotwo = (a + b) * c
    three = a * b + c
    threethree = a * (b + c)
    four = a * b * c

    print(max([one, two, twotwo, three, threethree, four]))


if __name__ == "__main__":
    main()
