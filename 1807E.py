#from sys import stdin, stdout

#input, print = stdin.readline, stdout.write


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(int(_) for _ in input().split())

        acc = [0 for _ in range(len(arr) + 1)]

        for i in range(len(arr)):
            acc[i + 1] = acc[i] + arr[i]

        solved = False

        left = 1
        right = len(arr)

        while not solved:
            mid = int((left + right) / 2)

            # print(mid)
            ammount = mid - left + 1

            # print(f"left: {left}, right: {right}, mid: {mid}")

            if left == right:
                print(f"! {left}")
                solved = True
                break

            expected_answer = acc[mid] - acc[left - 1]
            # print(expected_answer)

            ask = [str(i) for i in range(left, mid+1)]
            print(f"? {ammount} " + " ".join(ask))
            answer = int(input())

            if answer != expected_answer:
                right = mid
            else:
                if left == mid:
                    left = mid + 1
                else:
                    left = mid


if __name__ == "__main__":
    main()
