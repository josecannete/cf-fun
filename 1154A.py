def main():
    x = [int(_) for _ in input().split()]
    x.sort(reverse=True)

    print(f"{x[0] - x[1]} {x[0] - x[2]} {x[0] - x[3]}")


if __name__ == "__main__":
    main()
