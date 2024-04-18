inputNumber=int(input('Enter Number : '))

def reverse_number(inputNumber):                            #reversing the number
    reverse=0
    while inputNumber>0:
        remainder=inputNumber%10
        reverse=(reverse*10)+remainder
        inputNumber=inputNumber//10
    return reverse

if inputNumber == reverse_number(inputNumber):
    print('Yes',inputNumber,'is pallindrome number.')          # Pallindrome number
else:
    print('No',inputNumber,'is not pallindrome number.')


