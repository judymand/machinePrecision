
# Before calculating machine precision
print("\ncalculating without machine precision:")
print('abs(3.0*(4.0/3.0-1)-1) = ', abs(3.0*(4.0/3.0-1)-1))

# calculating machine precision
def machineEpsilon():
    epsilon = 1.0
    while (1.0 + 0.5 * epsilon) != 1.0:
        epsilon = 0.5 * epsilon
    print('abs(3.0*(4.0/3.0-1)-1) = ', abs(3.0*(4.0/3.0-1)-1+epsilon))

print("\ncalculating with machine precision:")
machineEpsilon()