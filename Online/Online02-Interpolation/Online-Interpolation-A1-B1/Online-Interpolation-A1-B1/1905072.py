import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def lower_bound(allPoints, n, value):
    low = 0
    high = n

    while low < high:
        mid = low + (high - low) // 2
        if value >= allPoints[mid].x:
            low = mid+1
        else:
            high = mid
    if low < n and allPoints[low].x < value:
        low += 1

    return low


def chooseNearestPoints(allPoints, n, value):
    # We need to choose n data points that are closest to 'value' , that also bracket 'value' to evaluate it.
    m = len(allPoints)
    if m < n or n < 2:
        return [False, None]
    pivot = lower_bound(allPoints, m, value)
    if pivot == 0 or pivot == m:
        # All the x Points are greater than value -> Can't be interpolated
        # All the x Points are smaller than value -> Can't be interpolated
        return [False, None]
    l = pivot-1
    r = pivot
    nearestPoints = np.zeros(shape=0, dtype=Point)
    nearestPoints = np.insert(nearestPoints, 0, allPoints[l])
    nearestPoints = np.append(nearestPoints, allPoints[r])
    for k in range(n-2, 0, -1):
        if l > 0 and r < m-1:
            if abs(allPoints[l-1].x-value) <= abs(allPoints[r+1].x-value):
                l -= 1
                nearestPoints = np.insert(nearestPoints, 0, allPoints[l])
            else:
                r += 1
                nearestPoints = np.append(nearestPoints, allPoints[r])
        elif l > 0:
            l -= 1
            nearestPoints = np.insert(nearestPoints, 0, allPoints[l])
        else:
            r += 1
            nearestPoints = np.append(nearestPoints, allPoints[r])
    return [True, nearestPoints]


def drawGraph(allPoints, n, a, b):
    x = np.array([allPoints[i].x for i in range(n)])
    y = np.array([allPoints[i].y for i in range(n)])
    plt.plot(x, y, marker='o')
    plt.annotate(f"({a:.2f},{b:.4f})", (a, b),
                 textcoords="offset points", xytext=(0, 10))
    plt.plot([a], [b], color='red', marker='o')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def interpolate(allPoints, value, n):
    status, nearestPoints = chooseNearestPoints(allPoints, n, value)
    if not status:
        return [False, None]
    print([i.x for i in nearestPoints])
    result = 0.0
    for i in range(n):
        Li = 1
        for j in range(n):
            if j != i:
                if nearestPoints[i].x == nearestPoints[j].x:
                    return [False, 0]
                Li *= ((value - nearestPoints[j].x) /
                       (nearestPoints[i].x - nearestPoints[j].x))
        result += Li*nearestPoints[i].y
    return [True, result]


def main():
    file = open("stock.txt", "r")
    lines = file.readlines()
    file.close()
    m = len(lines)-1
    allPoints = np.zeros(shape=m, dtype=Point)
    for i in range(m):
        a, b = map(float, lines[i+1].split())
        allPoints[i] = Point(a, b)
    value = float(input("Enter a day: "))
    # Quad
    status, quad = interpolate(allPoints, value, 3)
    if not status:
        print("Can't be calculated")
        return
    # Cube
    status, cube = interpolate(allPoints, value, 4)
    if not status:
        print("Can't be calculated")
        return
    print(f"Closing index : {cube:.4f}")
    print("Error: %.4f" % (abs((cube-quad)/cube)*100))
    drawGraph(allPoints, m, value, cube)


if __name__ == "__main__":
    main()
