a = input('Enter the file name : ')
try:
    b = open(a)
    c = b.read()
except:
    print('Enter a valid file name.')
    exit()
occurence = c.count(input('Enter the word you want :'))
print('No of occurence of the word is :',occurence)

