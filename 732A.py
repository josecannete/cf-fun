def main():
    k, r = (int(_) for _ in input().split())

    for i in range(1, 10):
        word = str(k * i)
        if word[-1] == "0" or word[-1] == str(r):
            print(i)
            break


if __name__ == "__main__":
    main()
