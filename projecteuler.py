#euler program
number =1
sum =0
while number <10:
    if number%3 ==0 or number%5==0:
        sum=sum+number
        number=number+1
        print(sum)
