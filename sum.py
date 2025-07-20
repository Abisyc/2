#summ of the integers
a=int(input('enter a the starting number'))
b=int(input('enter a the ending number'))
range(a,b)
s=0
for i in range(a,b+1):
    s=s+i
print(f'the sum of integers between {a} and {b} is :',s)