import sys


def circular_path(n: int, m: int) -> list[int]:
    path = []
    current = 1
    while True:
        path.append(current)
        end = (current - 1 + (m - 1)) % n + 1
        if end == 1:
            break
        current = end
    return path


def main():
    if len(sys.argv) != 5:
        print("Usage: python solution.py n1 m1 n2 m2", file=sys.stderr)
        sys.exit(1)

    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    result = circular_path(n1, m1) + circular_path(n2, m2)
    print("".join(map(str, result)))


if __name__ == "__main__":
    main()