import sys
import numpy as np
import matplotlib.pyplot as plt


def f(x: float):
    Cme = 5*10**(-4)
    numerator = -(6.73*x+6.725*10**(-8)+7.26*10**(-4)*Cme)
    denominator = (3.62*10**(-12)*x+3.908*10**(-8)*x*Cme)
    return numerator/denominator


# True error: 1/n^2
def trapezoidal(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    s *= h / 2
    return s


# True error: 1/n^4
def simpsons(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:    # Even
            s += 2*f(a+i*h)
        else:  # Odd
            s += 4*f(a+i*h)
    s *= h / 3
    return s


def trapezoidal_range(a, b, start, end):
    print("Sub-Intervals\tValue\t\t\tAbsolute Relative Approximate Error")
    oldS = 0
    for n in range(start, end+1):
        print(n, end="\t\t")
        s = trapezoidal(a, b, n)
        print(f'{s:4f}', end="\t\t")
        if n > 1:
            if s == 0:
                eA = abs((s-oldS)/(s+sys.float_info.epsilon))*100
            else:
                eA = abs((s-oldS)/s)*100
            print(f'{eA} %', end=" ")
        else:
            print("N/A", end=" ")
        print("")
        oldS = s


def simpsons_range(a, b, start, end):
    print("Sub-Intervals\tValue\t\t\tAbsolute Relative Approximate Error")
    oldS = 0
    for n in range(start, end+1):
        print(2*n, end="\t\t")
        s = simpsons(a, b, 2*n)
        print(f'{s:4f}', end="\t\t")
        if n > 1:
            if s == 0:
                eA = abs((s-oldS)/(s+sys.float_info.epsilon))*100
            else:
                eA = abs((s-oldS)/s)*100
            print(f'{eA} %', end=" ")
        else:
            print("N/A", end=" ")
        print("")
        oldS = s


def drawGraph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel("Concentration $(mol/cm^3)$")
    plt.ylabel("Time (seconds)")
    plt.show()


def main():
    a = 1.22*10**(-4)
    b = 0.5*a
    n = int(input())
    simpResult = 0
    trapResult = 0
    if n > 0:
        trapResult = trapezoidal(a, b, n)
        simpResult = simpsons(a, b, 2*n)

    # Trapezoidal
    print("Trapezoidal:")
    print(f'Using {n} subintervals: {trapResult:4f}')
    trapezoidal_range(a, b, 1, 5)

    # Simpsons
    print("Simpsons:")
    print(f'Using {2*n} subintervals: {simpResult:4f}')
    simpsons_range(a, b, 1, 5)

    # Graph
    x = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2])
    t = np.zeros(len(x))
    for i in range(len(x)):
        x[i] *= 10**(-4)
        t[i] = simpsons(a, x[i], 10)

    drawGraph(x, t)


if __name__ == "__main__":
    main()
