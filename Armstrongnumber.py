n = int(input("Please put a number in here:"))

sum = 0

temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if n == sum:
    print("This is a armstrong number.")
else:
    print("This is not an armstrong number")