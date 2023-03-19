from sys import stdin, stdout

input, print = stdin.readline, stdout.write


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(int(_) for _ in input().split())
        arr.sort()

        acc = 1

        printed_no = False

        if arr[0] != 1:
            print("NO\n")
            continue
        else:
            for i in range(1, len(arr)):
                a = arr[i]
                if acc < a:
                    print("NO\n")
                    printed_no = True
                    break
                else:
                    acc += a
            if not printed_no:
                print("YES\n")


if __name__ == "__main__":
    main()
