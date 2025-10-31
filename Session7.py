#Session 7 
# Create a Jupyter notebook, import matplotlib. Write cells that create an array x ranging from [0,1] in 100 steps and that defines a function that returns exp(x).  In a new cell use the function to set y=exp(x), and then plot x vs. y. Label the x-axis as “Time [milliseconds]” and the y-axis as “Awesomeness”. Save the figure as a PDF.  

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def my_exp(x):
    return np.exp(x)

y = my_exp(x)

#Plotting the defined x and y 
plt.figure(figsize=(5,5))
plt.plot(x, y, color='pink', linewidth = 1)

plt.xlabel("Time 'milliseconds'")
plt.ylabel("Awesomeness")
plt.title("Growth Graph y = exp(x)")
plt.grid(True)

#pdf publishing 
plt.tight_layout()
plt.savefig("Session7_exp_figure.pdf")
plt.show()