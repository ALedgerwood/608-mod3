import random

# producing 100 random numbers 
values = random.sample(range(1, 200), 100)

print('100 Random values from 1 to 200', values)

# getting the tools to calculate the variance
import statistics

# population variance
print('Population Variance is', statistics.pvariance(values))

# population standard deviation
print('Population Standard Deviation is', statistics.pstdev(values))

print('Alex Ledgerwood')