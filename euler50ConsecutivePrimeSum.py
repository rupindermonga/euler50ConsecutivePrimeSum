'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


def PrimeList(n):
    prime = [True for i in range(n+1)]
    p = 2
    prime_list = []
    while p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
            prime_list.append(p)
        p += 1
    return prime_list

def ConsecutivePrimeSum(n):
    prime_list = PrimeList(n)
    rev_prime_list = reversed(prime_list)
    max_count  = 0
    final_sum = 0
    for eachPrime in rev_prime_list:
        
        i = prime_list.index(eachPrime)
        if i < max_count:
           break
        else:
            for j in range(10):
                count = 0
                new_sum = 0
                for otherPrime in filter(lambda item: eachPrime, prime_list[j:]):
                    new_sum += otherPrime
                    count +=1
                    if new_sum >= eachPrime:
                        break
                if new_sum == eachPrime:
                    if max_count < count:
                        max_count = count
                        final_sum = new_sum
                        break
        
    return final_sum


final = ConsecutivePrimeSum(1000000)

print(final)
