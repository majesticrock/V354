import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x+b

werte = csv_read("csv/zeit-amplitude.csv")
xdata = np.zeros(16)
ydata = np.zeros(16)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] =np.log(float(values[1]))
        i+=1

x_line = np.linspace(14, 217)
plt.plot(xdata, ydata, "r.", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")

print(popt)
print(np.sqrt(pcov))

plt.xlabel(r"$t$ / µs")
plt.ylabel(r"$\ln\bigg(\frac{U_\text{C}}{1 \si{V}}\bigg)$")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot-amplitude.pdf")