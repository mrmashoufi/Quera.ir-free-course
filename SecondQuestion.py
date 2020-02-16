#Calculating Summation of Arithmetic progression
a , d , n = input().split() #You should input in one line and put space between each parameters
a = int(a) #a is initial term of an arithmetic progression
d=int(d) #d is the common difference of successive members
n=int(n) # n is the nth term of the sequence
output= int(n*((2*a)+(n-1)*d)/2)
print(output)
