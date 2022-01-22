import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x*x*x - 0.18*x*x + 0.0004752


def root(xL, xU, eS, maxIter):
    xM, xOldM = 0, 0
    for i in range(maxIter):
        xM = (xL+xU)/2
        yL = f(xL)
        yM = f(xM)
        if yL*yM < 0:
            xU = xM
        elif yL*yM > 0:
            xL = xM
        else:
            return xM
        if i > 0:
            eA = abs(xM-xOldM)*100/xM
            if eA <= eS:
                return xM
        xOldM = xM
    return xM


def table(xL, xU, eS, maxIter):
    print("Table:")
    print("Iteration No\t\tAbsolute Relative Approximate Error")
    xM, xOldM = 0, 0
    for i in range(maxIter):
        xM = (xL+xU)/2
        yL = f(xL)
        yM = f(xM)
        if yL*yM < 0:
            xU = xM
        elif yL*yM > 0:
            xL = xM
        else:
            return xM
        if i > 0:
            eA = abs(xM-xOldM)*100/xM
            print('{:12d}\t\t{:.6f}%'.format(i+1, eA))
            if eA <= eS:
                return xM
        else:
            print('{:12d}\t\tCannot be calculated'.format(i+1))
        xOldM = xM


def drawGraph():
    x = np.array(np.arange(0, 0.13, 0.01))
    y = np.array([f(x[i]) for i in range(13)])
    plt.plot(x, y, marker='o')
    plt.grid()
    plt.title("f(x)=x^3 - 0.18x^2 + 4.752x10^-4")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


def main():
    drawGraph()
    xL = float(input("Estimate lower bound: "))
    xU = float(input("Estimate upper bound: "))
    maxIter = int(input("Enter max allowed iteration: "))
    print("Depth of the submerged ball is {:.6f}  meter".format(
        root(xL, xU, 0.5, maxIter)))
    table(0, 0.12, 0.5, 20)


if __name__ == "__main__":
    main()
# x^3 - 0.18x^2 + 4.752x10^-4
