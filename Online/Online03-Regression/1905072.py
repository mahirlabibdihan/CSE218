import numpy as np
import matplotlib.pyplot as plt


def linear(x, y):
    n = np.size(x)
    p = np.sum(x*x)
    q = np.sum(x)
    r = np.sum(x*y)
    s = np.sum(y)
    d = (n*p - q*q)
    a_1 = (n*r - q*s) / d
    a_0 = (p*s - q*r) / d
    return (a_0, a_1)


def main():
    x = np.array([0, 5, 10, 15, 20, 25, 30])
    y = np.array([1000, 550, 316, 180, 85, 56, 31])
    # Exponential to Linear
    a_0, a_1 = linear(x, np.log(y))
    a = np.exp(a_0)
    b = a_1
    print(f'Best-fit Model: y = {a:.4f}e^({b:.4f}x)')
    hours = 40
    drugs = a*np.exp(b*hours)
    print(f'Amount of drug in body after {hours} hours: {drugs:.4f} mg')

    # Graph for visualization
    plt.scatter(x, y, color='green')
    x = np.append(x, hours)
    y_pred = a * np.exp(b*x)
    plt.plot(x, y_pred)
    plt.annotate(f"({hours},{drugs:.4f})", (hours, drugs),
                 textcoords="offset points", xytext=(0, 10), horizontalalignment='right')
    plt.scatter([hours], [drugs], color='red')
    plt.title("Drug in Body After Specific Time")
    plt.xlabel("Hours Since Drug was Administered")
    plt.ylabel("Amount of Drug in Body(mg)")
    plt.legend([f'y = {a:.4f}e^({b:.4f}x)', 'Given Values',
               'Predicted Value'], loc="upper right")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
