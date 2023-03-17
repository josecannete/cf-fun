def main():

    guest = input()
    resident = input()
    pile = input()

    word = guest + resident
    word = list(word)
    word.sort()
    pile = list(pile)
    pile.sort()

    if word == pile:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
