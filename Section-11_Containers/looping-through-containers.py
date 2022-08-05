primes = [2, 3, 5, 7, 11]

#for number in primes: 
#    print(number)

#index = 0
#while index < len(primes):
#    print(primes[index])
#    index += 1

#even_numbers = []
#odd_numbers = []

#for number in primes:
#    if number % 2 == 0:
#        #print(f"{number} is even")
#        even_numbers.append(number)
#    else:
        #print(f"{number} is odd")
#        odd_numbers.append(number)

#print("Even number(s): ")
#for i in even_numbers:
#    print(i)

#print("Odd number(s): ")
#for j in odd_numbers:
#    print(j)

ssn_name_pairs = {"123-456-789": "John Appleseed",
                  "000-000-002": "Dwight Schrute",
                  "000-000-003": "Pam Beesly"}

keys = ssn_name_pairs.keys()
values = ssn_name_pairs.values()

print("Dictionary keys: ")
for key in keys:
    print(key)

print("Dictionary values: ")
for value in values:
    print(value)

key_value_pairs = ssn_name_pairs.items()

print("Key-value pairs")
for (key, value) in key_value_pairs:
    print(key, value)