import numpy as np

N = 6
fea_vec = np.random.rand(1, N)

# Compute the mean and variance
mean = np.mean(fea_vec)
variance = np.var(fea_vec)
                   
# Output the results
print("Feature Vector:", fea_vec)
print("Mean of the Feature Vector:", mean)
print("Variance of the Feature Vector:", variance)
