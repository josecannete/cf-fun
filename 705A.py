def main():
    n = int(input())

    odd = "I hate"
    even = "I love"
    connector = " that "

    sentiment = ""

    for i in range(n):
        if (i + 1) % 2 == 1:
            sentiment += odd
        else:
            sentiment += even
        if i + 1 != n:
            sentiment += connector

    print(sentiment + " it")


if __name__ == "__main__":
    main()
