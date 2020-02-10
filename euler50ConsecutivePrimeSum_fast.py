'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


def PrimeList(n):
    # Create a candidate list within which non-primes will
    # marked as None, noting that only candidates below
    # sqrt(n) need be checked. 
    candidates = list(range(n+1))
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    # If the current candidate is already checked off then
    # continue to the next iteration.
    for i in range(2, fin+1):
        if not candidates[i]:
            continue
 
        candidates[2*i::i] = [None] * (n//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]


def ConsecutivePrimeSum(n):
    prime_list = PrimeList(n)
    
    final_list = []
    for start in range(10):
        seq = prime_list[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > 1000000:
                break
            i += 1
            if total in prime_list:
                c = seq[:i]
                if len(c) > len(final_list):
                    final_list = c
    return sum(final_list)

final = ConsecutivePrimeSum(1000000)

print(final)

