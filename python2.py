#this program will check wethe rthe number is prime or not
number= int(input("enter the number:"))
# define a flag variable
flag = False
# prime numbers are greater than 1
if number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")