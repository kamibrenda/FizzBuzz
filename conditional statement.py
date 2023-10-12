#For every number divisible by 4 it prints Fizz and if divisible by 5 it prints Buzz.
for num in range (1,201):
    string = ""
    if num % 4 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 4 != 0 and num % 5 != 0:
        string = string + str(num)

    print(string)