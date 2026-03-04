n = int(input("Please put a number here:"))
m = 0
temp = n
while temp > 0:
    temp = temp//10
    m = m+1
print("There are", m, "digit(s) in", n)