from math import sqrt
import matplotlib.pyplot as plt
n = int(input('Enter n: '))
prime = [True] * n
prime[0] = prime[1] = False

pi = [0] * n
count = 0

for i in range(2, n):
    if prime[i]:
        count +=1
        for j in range (i * i, n, i):
            prime[j] = False
        pi[i] = count

for i in range(n):
    if prime[i]:
        print(i)

plt.figure(figsize = (8,8))
plt.plot[range(n), pi]
plt.plot([0, n - 1], [0, count])
plt.show()
