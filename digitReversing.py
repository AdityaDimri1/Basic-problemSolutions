def reverse_number(num):
    reverse=0
    while num>0:
        remainder=num%10
        reverse=(reverse*10)+remainder
        num=num//10
    return reverse

# Example ==>
reversValue=reverse_number(34578)
print(reversValue)