a = int(input('Enter the number : '))
if(a==2 or a==3):
    print('Prime')
    exit()
for i in range(2,int(a/2)+1):
    if(a%i==0):
        print('Not prime')
        exit()
print('Prime')