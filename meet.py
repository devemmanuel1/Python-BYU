print("Enter a list of numbers, type 0 when finished.")
number = -1

sum = 0
largest_number = 0
smallest_number = 0
numbers = []

while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)
        sum+=number

        if number > largest_number:
            largest_number = number

print(f'The sum is: {sum}')

count = len(numbers)
average = sum / count
print(f"The average is: {average}")

# print(f'The averange is : { sum / len(numbers)}')

print(f'The largest number is: {largest_number}')


for number in numbers:
    if number < largest_number and number > 0:
        smallest_number = number

print(f'The smallest positive number is: {smallest_number}')

numbers.sort()

print('The sorted list is:')

for number in numbers:
    print(number)