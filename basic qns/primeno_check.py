"""input = int(input("enter a number: "))

if input % 2 == 0:
    print("even number")
else:
    print("odd number")
    """

    
#optimised program

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

input = int(input("Enter a number: "))
if is_prime(input):
    print("Prime number")
else:
    print("Not a prime number")
