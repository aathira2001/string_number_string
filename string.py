word = input("Enter the string")
arr = []
arr.append(word)
count = len(word)- 2 
if len(word)>100:
    print(word[0],count,word[-1])
else:
    print(word)
