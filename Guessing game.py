import random
num = random.randint(1,9)
while(True):
    n = int(input('Please guess the number'))
    if (n>9)or(n<1):
        print('Please guess between 1 to 9')
    elif(n==num):
        print('You guessed it correct.')
        break
    elif(n==(num-1))or(n==(num+1)):
        print('Very close')
    elif(n==(num-2))or(n==num+2):
        print('Close')
    elif (n==num-3) or (n==num-4) or (n==num+3) or (n==num+4):
        print('Far')
    else:
        print('Very far')