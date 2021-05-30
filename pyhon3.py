number= int(input("enter the number:"))
index=2
while index< number:
    if number% index == 0 :
        print("{number} is not prime number")
        breakindex= index+1
        #else:
            #print("{number} is prime number")

