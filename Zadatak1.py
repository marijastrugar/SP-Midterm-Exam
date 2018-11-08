sum = 0
count = 0
number = input("Enter a number: ")
if number != '=':
    number = int(number)
while number != '=':
    if number % 5 != 0 and number % 3 == 0:
        sum += number
        count += 1
    number = input("Enter a number: ")
    if number != '=':
        number = int(number)
print("Arithmetic mean: " + str(sum/count) if count > 0 else str(0))