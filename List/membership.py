"""
in - True/false
not in - opposite
"""
'''STR = ["hi", "hello", "bye", "goodbye",1 , 5.61]
check = input("Enter the value to check: ")
if check in STR:
    print(f"{check} is present in the list")
else:
    print(f"{check} is not present in the list")'''

STR = ["hi", "hello", "bye", "goodbye",1 , 5.61]
check = input("Enter the value to check: ")
if check not in STR:
    print(f"{check} is not present in the list")    
else:
    print(f"{check} is present in the list")