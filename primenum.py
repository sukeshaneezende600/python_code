# you have to print first 10 prime numbers and store it into an array and then reverse the array and print it write a program
#most asked question :

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num** 0.5) +1):
        if num % i == 0:
            return False
        return True
    
prime_numbers =[]
num = 2

while len(prime_numbers) < 10:
    if isprime(num):
        prime_numbers.append(num)
    num +=1
print("Prime numbers:", prime_numbers)

prime_numbers.reverse()
print("reversed prime numbers:", prime_numbers)



