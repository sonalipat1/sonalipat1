number =int(input("Enter number to cal larger prime number"))
index= number//2
while index>=2:
    if number% index ==0:
        prime_index=2
        while prime_index<=(index//2):
            if(index% prime_index==0):
                break
            prime_index +=1
        else:
                print(f"{index} is larget prime factor")
                break
    index -=1