def main():
    t = int(input())

    for _ in range(t):
        _ = input()
        word = input()

        dic = {}
        for i in range(len(word)):
            dic[word[i]] = dic.get(word[i], list())
            dic[word[i]].append(i % 2)

        printed_no = False

        for _, value in dic.items():
            if len(set(value)) > 1:
                print("NO")
                printed_no = True
                break

        if not printed_no:
            print("YES")


if __name__ == "__main__":
    main()
