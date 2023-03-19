def main():
    n = int(input())

    goals = {}

    for _ in range(n):
        word = input()
        goals[word] = goals.get(word, 0) + 1

    goals = list(goals.items())
    goals.sort(key=lambda x: x[1], reverse=True)
    print(goals[0][0])


if __name__ == "__main__":
    main()
