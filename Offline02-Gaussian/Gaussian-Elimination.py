import numpy as np


def f(x, y):
    return [x, y, 1], -x*x-y*y


def partialPivot(A, n, k):
    absMaxIdx = k
    for i in range(k, n):
        if abs(A[i][k]) > abs(A[absMaxIdx][k]):
            absMaxIdx = i
    if absMaxIdx != k:
        # A[j], A[absMaxIdx] = np.array(A[absMaxIdx]), np.array(A[j])
        A[[k, absMaxIdx], :] = A[[absMaxIdx, k], :]


def printMatrix(A, n):
    print("A matrix:")
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:.4f}", end=" ")
        print("")
    print("")
    print("B matrix:")
    for i in range(n):
        print(f"{A[i][n]:.4f}")
        # print(round(A[i][n], 4))
    print("")


def GaussianElimination(A, B, pivot=True, showall=True):
    n = len(A)
    x = np.zeros(n)
    A = np.append(A, B, axis=1)
    # Forward elimination
    for k in range(0, n-1):  # goes down -> (n-1) steps
        if pivot:
            partialPivot(A, n, k)
        # A[absMaxIdx][j] == 0
        if A[k][k] == 0:
            return [False, x]
        if showall:
            print('Step {:d}:'.format(k+1))
        for i in range(k+1, n):   # goes right -> i sub steps
            factor = A[i][k]/A[k][k]
            for j in range(n+1):
                A[i][j] = A[i][j] - factor*A[k][j]
            if showall:
                print('Sub Step {:d}:'.format(i-k))
                printMatrix(A, n)
    # Back substitution
    for i in range(n-1, -1, -1):
        if A[i][i] == 0:
            return [False, x]
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] = x[i]-x[j]*A[i][j]
        x[i] = x[i]/A[i][i]
    return [True, x]


def main():
    n = 3
    # n = int(input())
    A = np.zeros((n, n))
    B = np.zeros((n, 1))
    # for i in range(n):
    #     A[i] = np.array([list(map(float, input().split()))], float)
    # for i in range(n):
    #     B[i][0] = float(input())

 

    temp = f(-2, 0)
    A[0], B[0] = temp[0], temp[1]
    temp = f(-1, 7)
    A[1], B[1] = temp[0], temp[1]
    temp = f(5, -1)
    A[2], B[2] = temp[0], temp[1]

    status, x = GaussianElimination(A, B)
    if status:
        print("Solution:")
        for i in x:
            print(f"{i:.4f}")
    else:
        print("No solution exists")


if __name__ == '__main__':
    main()

'''
-2a + 0b + c = -4
-a  + 7b + c = -50
5a  -  b + c = -26
3
-2  0 1
-1  7 1
 5 -1 1
-4
-50
-26
'''
