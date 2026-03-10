
#example 1 simple method 
numbers=[22,9,8,77,56,10,23,3,43,44,74,33,13,23]
even_numbers =[num for num in numbers if num % 2 == 0]
odd_numbers =[num for num in numbers if num % 2 !=0]

print("Even numbers:",even_numbers)
print("Odd numbers:", odd_numbers)


#Example2 using Append Method:

numbers =[20,41, 63, 22, 28, 99,67, 7, 588,48]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
