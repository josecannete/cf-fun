def main():
    _ = input()
    scores = list(int(_) for _ in input().split())
    amazings = 0
    worst = best = scores[0]

    for score in scores:
        if score < worst:
            amazings += 1
            worst = score
        elif score > best:
            amazings += 1
            best = score

    print(amazings)


if __name__ == "__main__":
    main()
