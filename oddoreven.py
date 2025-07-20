a=int(input('enter a integer '))
if a==0 :
    print('enter a different number')
elif float(a/2) == int(a/2):
    print(f'{a} is an even number')
else :
    print(f'{a} is an odd number')