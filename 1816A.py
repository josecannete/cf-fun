def next_primo(num, primos):
    # print(num)
    for i in range(num + 1, 10000000000):
        is_primo = True
        for primo in primos:
            if i % primo == 0 and i != primo:
                is_primo = False
                break
        if is_primo is False:
            continue
        else:
            return i


def before_primo(num, primos):
    # print(num)
    for i in range(num, 1, -1):
        is_primo = True
        for primo in primos:
            if i % primo == 0 and i != primo:
                is_primo = False
                break
        if is_primo is False:
            continue
        else:
            return i


def criba_eratostenes(n):
    primos = []
    no_primos = []

    for i in range(2, n + 1):
        if i not in no_primos:
            primos.append(i)

            for j in range(i * i, n + 1, i):
                no_primos.append(j)

    return primos


def main():
    # primos = criba_eratostenes(10000)
    # print(primos)
    t = int(input())
    for _ in range(t):
        a, b = (int(_) for _ in input().split())

        if a == 1 or b == 1:
            print(1)
            print(f"{a} {b}")
        else:
            # y1 = before_primo(b, primos)
            # x1 = a - next_primo(b - y1, primos)
            x1 = 1
            y1 = b - 1
            print(2)
            print(f"{x1} {y1}")
            print(f"{a} {b}")


if __name__ == "__main__":
    main()
