# draw pyramid using *

#     *
#    * *
#   * * *

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    # printing spaces
    print(" " * (rows - i), end="")
    # printing stars
    print("* " * i) 
    