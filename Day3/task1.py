def generate_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
"""The function first creates an empty list primes to store the prime numbers.
 It then uses a for loop to iterate over all numbers from 2 to n. For each number, 
 the function checks whether it is prime by testing whether it is divisible by any number between 2 and its square root (inclusive). 
 If the number is prime, it is added to the primes list.

Finally, the function returns the primes list containing all prime numbers less than or equal to n.

You can call the function by passing a positive integer n as an argument, like this:
"""
primes = generate_primes(20)
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
"""

This will generate a list of all prime numbers less than or equal to 20 and store it in the primes 
variable, which is then printed to the console."""