def main():
    n = int(input())
    count = 0

    faces = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20,
    }

    for _ in range(n):
        word = input()
        count += faces[word]

    print(count)


if __name__ == "__main__":
    main()
