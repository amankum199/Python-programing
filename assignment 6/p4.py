#Write a program to calculate sum of squares of first N natural numbers
a=int(input("Enter number: "))
sum=0
for i in range(1,a+1,1):
    sum=sum+i*i
print(sum)
