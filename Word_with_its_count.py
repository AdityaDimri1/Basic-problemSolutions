wordCount={}

userInput=int(input('Enter the no of string : '))   
for num in range(0,userInput):
    stringInput=input('Enter the string : ')
    if stringInput in wordCount:
        wordCount[stringInput]+=1
    else:
        wordCount[stringInput]=1 
print(wordCount)