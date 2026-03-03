number = int(input("Please enter a number here:"))
rev = 0

temp = number 

while temp > 0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)
if rev == number:
    print("The number is a palindrome")
else:
    print("the number is not a palindrome")