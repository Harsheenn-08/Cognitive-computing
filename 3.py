import random

random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = [num for num in random_numbers if num % 2 != 0]
even_numbers = [num for num in random_numbers if num % 2 == 0]

def checkPrime(num):
        for i in range(2,num//2+1):
            if num%i==0:
                return 0
        return 1

prime_numbers = [num for num in random_numbers if checkPrime(num)]

print("Odd numbers ",odd_numbers)
print("Even numbers",even_numbers)
print("Prime numbers ",prime_numbers)
