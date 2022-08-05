primes = [2, 3, 5, 7, 11]
print(primes)
primes[1] = 17
print(primes)

primes.append(13)
print(primes)

characters = []
characters.append("a")
print(f"The length of the characters list is: {len(characters)}")

primes.insert(1, 3)
print(primes)

n = primes.pop(2)
print(f"Element {n} removed.  The primes list became {primes}")

primes.remove(5)
print(primes)