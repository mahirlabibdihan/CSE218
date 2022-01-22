import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def drawGraph(f, n, a, b):
    x = np.array([f[i].x for i in range(n)])
    y = np.array([f[i].y for i in range(n)])
    plt.plot(x, y, marker='o')
    plt.annotate(f"({a:.2f},{b:.4f})", (a, b),
                 textcoords="offset points", xytext=(0, 10))
    plt.plot([a], [b], color='red', marker='o', markersize=10)
    plt.plot([0, a, a], [b, b, 0], linestyle="dashed")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def productTerm(i, value, x):
    pro = 1
    for j in range(i):
        pro *= (value - x[j])
    return pro


def dividedDiffTable(f, n):
    print("Table:")
    table = np.zeros(shape=(n, n))
    for i in range(n):
        table[i][0] = f[i].y
    for i in range(1, n):
        for j in range(0, n - i):
            if f[j].x == f[i + j].x:
                return [False, None]
            table[j][i] = ((table[j + 1][i - 1]-table[j]
                           [i - 1]) / (f[i + j].x-f[j].x))
    return [True, table]


def applyFormula(value, x, table, n):
    sum = 0
    for i in range(0, n):
        sum += (productTerm(i, value, x) * table[0][i])
    return sum


def printDiffTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print("%10.4f" % y[i][j], end="  ")
        print("")


def lower_bound(f, n, value):
    low = 0
    high = n

    while low < high:
        mid = low + (high - low) // 2
        if value >= f[mid].x:
            low = mid+1
        else:
            high = mid
    if low < n and f[low].x < value:
        low += 1

    return low


def nearestPoints(f, n, value):
    # We need to choose n data points that are closest to 'value' , that also bracket 'value' to evaluate it.
    m = len(f)
    if m < n or n < 2:
        return [False, None]
    pivot = lower_bound(f, m, value)
    print(pivot)
    if pivot == 0 or pivot == m:
        # All the x Points are greater than value -> Can't be interpolated
        # All the x Points are smaller than value -> Can't be interpolated
        return [False, None]
    l = pivot-1
    r = pivot
    xy = np.zeros(shape=0, dtype=Point)
    xy = np.insert(xy, 0, f[l])
    xy = np.append(xy, f[r])
    for k in range(n-2, 0, -1):
        if l > 0 and r < m-1:
            if abs(f[l-1].x-value) <= abs(f[r+1].x-value):
                l -= 1
                xy = np.insert(xy, 0, f[l])
            else:
                r += 1
                xy = np.append(xy, f[r])
        elif l > 0:
            l -= 1
            xy = np.insert(xy, 0, f[l])
        else:
            r += 1
            xy = np.append(xy, f[r])
    return [True, xy]


def interpolate(f, value, n, show=True):
    status, xy = nearestPoints(f, n, value)
    if not status:
        return [False, None]
    status, table = dividedDiffTable(xy, n)
    if not status:
        return [False, None]
    if show:
        printDiffTable(table, n)
    x = np.array([i.x for i in xy])
    result = applyFormula(value, x, table, n)
    return [True, result]


def main():
    file = open("gene.txt", "r")
    lines = file.readlines()
    file.close()
    m = len(lines)
    f = np.zeros(shape=m, dtype=Point)
    for i in range(m):
        a, b = map(float, lines[i].split())
        f[i] = Point(a, b)
    value = float(input())
    # Quad
    status, quad = interpolate(f, value, 3)
    if not status:
        print("Can't be calculated")
        return
    # Cube
    status, cube = interpolate(f, value, 4)
    if not status:
        print("Can't be calculated")
        return
    print(f"Value is : {cube:.4f} {quad:.4f}")
    print("Error: %.4f" % (abs((cube-quad)/cube)*100))
    drawGraph(f, m, value, cube)


if __name__ == "__main__":
    main()

'''
4
10 227.04
15 362.78
20 517.35
22.5 602.97
16
'''
