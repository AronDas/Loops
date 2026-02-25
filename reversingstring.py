a = input("Please put your own sentence here:")

string2 = ('')
for i in a:
    string2 = i + string2

print("\nThe original sentence is:", a)
print("The reversed sentence is:", string2)