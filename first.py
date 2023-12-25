a=1
b=int(input('Enter the limit :'))
while a<=b:
    if a%15==0:                     
        print('fizzBuzz')
    elif a%5==0:
        print('buzz')
    elif a%3==0 :
        print('fizz')
    else:
        print(a)
    a+=1
          