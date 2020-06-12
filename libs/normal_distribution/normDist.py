#!/usr/bin/env python

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


sigma       = 1
mu          = 0
n_points    = 1000

y_values = mu +  sigma * np.random.randn( n_points )
plt.hist(y_values, density= True)

x_values = np.linspace( mu - 3*sigma, mu + 3*sigma, n_points )
plt.plot( x_values, stats.norm.pdf ( x_values, mu, sigma ) )


plt.show()

