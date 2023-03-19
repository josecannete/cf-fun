from sys import stdin, stdout

input, print = stdin.readline, stdout.write


def main():
    t = int(input())

    for _ in range(t):
        n, q = (int(_) for _ in input().split())

        arr = [int(_) for _ in input().split()]
        acc = [0 for _ in range(len(arr) + 1)]

        for i in range(len(arr)):
            acc[i + 1] = acc[i] + arr[i]

        for _ in range(q):
            l, r, k = (int(_) for _ in input().split())

            left_sum = acc[l - 1]
            right_sum = acc[-1] - acc[r]

            in_between = (r - l + 1) % 2
            k = k % 2

            if (left_sum % 2 + right_sum % 2 + k * in_between) % 2 == 1:
                print("YES\n")
            else:
                print("NO\n")


if __name__ == "__main__":
    main()
