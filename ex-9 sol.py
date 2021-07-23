

import matplotlib.pyplot as plt
import numpy as np
import math

L = [0.2, 0.6, 1, 2, 3, 4, 6, 8, 10]

mu_e = 18

R_e = 5

R = np.arange(0,200,0.1)

I_e = 10**(-mu_e/2.5)

for n in L:

    b_n = 2*n - 1/3 + 4/(405*n) + 46/(25515*n**2)

    magnitude = []
    for r in R:
        magnitude.append(-2.5 * np.log10(I_e * np.exp(-b_n*((r/R_e)**(1/n)-1))))

    #plt.plot(R,magnitude)
    plt.semilogx(R, magnitude)     #For log x-axis

plt.xlabel("radius")
plt.ylim(30, 5)
plt.xlim(0,200)
plt.ylabel("magnitude")
plt.title('For n=%f' %n)
plt.show()