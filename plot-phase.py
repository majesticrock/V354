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
    re = np.arctan(( x*R*C )/( 1 - L*C*x**2 ))
    for k in range(len(re)):
        if(re[k] < 0):
            re[k] += np.pi
    
    return re

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
        ydata[i] = float(values[2]) * float(values[0]) * 2 * np.pi *10**(-3)
        i+=1

x_line = np.linspace(12, 62)*2*np.pi * 10**(-2)
plt.plot(xdata, ydata, "r.", label="Messwerte")
#popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, 271.6, 3.53*10**(-3), 5.015*10**(-9)), "b-", label="Theoriekurve")

plt.xticks(np.array([0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00]))
plt.yticks(np.array([0, 0.25, 0.50, 0.75, 1.00]) * np.pi, [r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.xlabel(r"$\omega$ / $10^{5}$ Hz")
plt.ylabel(r"$\phi$ / rad")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-phase.pdf")