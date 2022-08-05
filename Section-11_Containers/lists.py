primes = list()

primes = [2, 3, 5, 7, 11]
primes.append(13)
primes.append(17)
#print(primes)

names = ["Michael", "Dwight", "Pam"]

values = [True, False, False, True]

bag = [1, 2, 3]
bag.append("Pam")
bag.append(True)
bag.append(4)

#print(bag)


list = ["Michael", "Dwight", "Pam"]
name = list[2]

# 0 <= valid_index < len(list)

def is_valid_index(index: int, list: list) -> bool:
    result = False
    if 0 <= index and index < len(list):
        result = True
    return result

index = 2
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is out of range.")