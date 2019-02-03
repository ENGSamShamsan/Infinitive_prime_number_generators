

# Infinitive prime number generators


import math
import time
import itertools

def prime_finder(n):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
    return is_prime

for x in itertools.count():
    if prime_finder(x):
        print(x,"   .....",)
        time.sleep(0.1)


