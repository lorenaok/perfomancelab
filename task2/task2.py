import sys


def main():
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(ellipse_file, "r") as f:
        tokens = f.read().split()
    x0, y0, a, b = map(float, tokens[:4])

    with open(points_file, "r") as f:
        data = f.read().split()

    result = []
    eps = 1e-9

    for i in range(0, len(data) - 1, 2):
        x = float(data[i])
        y = float(data[i + 1])

        value = ((x - x0) / a) ** 2 + ((y - y0) / b) ** 2

        if abs(value - 1.0) <= eps:
            result.append("0")
        elif value < 1.0:
            result.append("1")
        else:
            result.append("2")

    print("\n".join(result))


if __name__ == "__main__":
    main()