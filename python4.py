numberofterms= int(input("enter the number:"))
counter = 0
first = 0
second = 1
temp = 0
while counter <= numberofterms:
    print(first)
temp = first + second
first = second
second = temp
counter = counter + 1

