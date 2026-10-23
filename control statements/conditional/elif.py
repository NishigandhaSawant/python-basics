age = int(input("Enter your age: "))
if (age >= 18 and age < 100):
    print("You are eligible to vote.")
elif age >= 100:
    print("You are eligible to vote, but you are quite old!")
elif age <= 0:
    print("Invalid age entered.")

else:
    print("You are not eligible to vote.")
