import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, R, L, C):
    x = x*10**(5)
    return 1/np.sqrt( ( 1 - L*C*x**2 )**2 + x**2 * R**2 * C**2)

werte = csv_read("csv/var-freqU=6.55.csv")
xdata = np.zeros(31)
ydata = np.zeros(31)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0]) * 10**(-2) *2*np.pi
        ydata[i] = float(values[1]) / 6.55
        i+=1

guess = [271.6, 3.53*10**(-3), 5.015*10**(-9)]

x_line = np.linspace(12, 62)*2*np.pi  * 10**(-2)
plt.plot(xdata, ydata, "r.", label="Messwerte")
plt.plot(x_line, func(x_line, 271.6, 3.53*10**(-3), 5.015*10**(-9)), "b-", label="Theoriekurve")


plt.xticks(np.array([0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00]))
plt.xlabel(r"$\omega$ / $10^{5}$ Hz")
plt.ylabel(r"$\frac{U_\text{C}}{U_0}$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-guete.pdf")