def sieve_of_erastosthenes(n):
    # Create a boolean array of entries a True value means the number is prime
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # Check if the current number is prime
        if prime[p - 1] == True:
            # Update all multiples of p starting from p^2
            for i in range(p * p, n+1, p):
                prime[i -1] = False
        p += 1
    
    #Filter out all False values
    return [i + 1 for i in range(n) if prime[i] == True]

if __name__ == '__main__':
    print(sieve_of_erastosthenes(50))