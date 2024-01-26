import numpy as np


def getNumber(prompt):
    while True:
        try:
            value = input(prompt)
            if value == "":
                raise ValueError("Missing input!")
            value = float(value)
            break
        except ValueError:
            print(f"'{value}' is not a number!")
        except:
            print("Invalid input!")
    return value


def yonellipse(a, b, xValues):
    return b * np.sqrt(1 - np.square(xValues / a))


def verifypoints(a, b, xValues, yValues):
    return np.isclose(np.divide(np.square(xValues), np.square(a)) + np.divide(np.square(yValues), np.square(b)), 1)


def main():
    a = getNumber("Enter the length of the major axis: ")
    b = getNumber("Enter the length of the minor axis: ")
    num_points = getNumber("Enter the number of points along the major axis: ")
    xValues = np.linspace(0, a, num_points)
    yValues = yonellipse(a, b, xValues)
    points_on_ellipse = verifypoints(a, b, xValues, yValues)
    print("X-Values\tY-Values\tOn Ellipse")
    for x, y, on_ellipse in zip(xValues, yValues, points_on_ellipse):
        print(f"{x:.4f}\t\t{y:.4f}\t\t{on_ellipse}")
        

if __name__ == '__main__':
    main()

