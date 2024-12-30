# WAP to display prime numbers from 1 to 100

# here i am using the most efficient algorithm saive of eratosethenes

def prime_number(n):
   
    prime = (n+1)*[True]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    for i in range(2, n+1):
        if prime[i]:
            print(i, end=' ');

prime_number(100);