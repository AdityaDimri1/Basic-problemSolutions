for i in range(1,6):
    print(i*'*')

for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()


i=5
for j in range(0,i):
    print(i*'*')
    i-=1

for i in range(0,5):
    for j in range(1,6-i):
        print('*',end='')
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end='')
    print()

for i in range(0,5):
    for j in range(1,6-i):
        print(j%2,end='')
    print()
                                                    

