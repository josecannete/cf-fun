def main():
    _ = input()
    word = input()

    anton = 0
    danik = 0

    for char in word:
        if char == "A":
            anton += 1
        else:
            danik += 1

    if anton > danik:
        print("Anton")
    elif anton < danik:
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    main()
