# Wap to display the prime numbers 1 to 100
from math import ceil, sqrt

def list_primes(n1, n2):
    for num in range(n1, n2):
        flag = 0
        for i in range(2, ceil(sqrt(num)) ):
            if num % i == 0:
                flag = 1
                break
        if flag == 0 and num > 1:
            print(num,end=' ')

list_primes(1, 101)