start = int(input("Enter start value: "))
stop=int(input("Enter stop value: "))
skip = int(input("Enter skip value: "))
for i in range(start,stop):
    if i == skip:
        continue
    print(i)