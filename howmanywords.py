a1 = input("Please enter a sentence.")

total = 1
for i in range(len(a1)):
    if(a1[i] == ' ' ):
        total = total + 1

print("total number of words in this sentence are", total)