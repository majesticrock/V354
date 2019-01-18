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
        xdata[i] = float(values[0]) * 10**(3) *2*np.pi
        ydata[i] = float(values[1]) / 6.55
        i+=1

guess = [271.6, 3.53*10**(-3), 5.015*10**(-9)]

x_line = np.linspace(12 * 10**(3), 62 * 10**(3))*2*np.pi
plt.plot(xdata, ydata, "r.", label="Messwerte")
#popt, pcov = curve_fit(func, xdata, ydata, guess)
plt.plot(x_line, func(x_line, 271.6, 3.53*10**(-3), 5.015*10**(-9)), "b-", label="Theoriekurve")
#plt.plot(x_line, func(x_line, *popt), "g-", label="Fit")

#print(popt)
#print(np.sqrt(pcov))

plt.xlabel(r"$\omega$ / $\frac{1}{\symup{s}}$")
plt.ylabel(r"$\frac{U_C}{U_0}$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-guete.pdf")