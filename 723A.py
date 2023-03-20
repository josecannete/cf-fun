def main():
    x1, x2, x3 = (int(_) for _ in input().split())

    points = [x1, x2, x3]
    points.sort()

    mid_point = points[1]

    distance = abs(x1 - mid_point) + abs(x2 - mid_point) + abs(x3 - mid_point)

    print(distance)


if __name__ == "__main__":
    main()
