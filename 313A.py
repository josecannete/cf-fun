def main():
    word = input()

    opt_one = int(word[:-1])
    opt_two = int(word[:-2] + word[-1])
    opt_three = int(word)

    print(max(opt_one, opt_two, opt_three))


if __name__ == "__main__":
    main()
