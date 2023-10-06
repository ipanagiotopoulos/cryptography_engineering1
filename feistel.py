alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listAlphabet = list(alphabet)

inp = input("Enter Text : ")
round = int(input("Round : "))
newList = []

for i in inp:
    newList.append(listAlphabet.index(i))

#"".join(newList)
print(newList)

flag = 0
while flag != 1:
    if(len(newList) % 16 != 0):
        newList.append(0)
    else:
        flag = 1

print(newList)



iteration = 1
firstIndex = 0
lastIndex = (iteration*16)
cipher = []
cipCount = 0
length = len(newList)
area = []
while True:
    if(lastIndex > length):
        print("control")
        break
    mid = int((lastIndex - firstIndex / 4))
    
    area = newList[firstIndex:lastIndex]
    
    firstIndexArea = 0
    #lastIndexArea = len(area) - 1
    midArea = int(len(area) / 2)
    left_half = area[firstIndexArea:midArea]
    right_half = area[midArea:len(area)]
    
    for i in range(0, round):
        
        print("left half : " + str(left_half))
        print("right half : " + str(right_half))
        if (i != round - 1):
            tmp = right_half
            right_half = [(x+round*y)%26 for x,y in zip(left_half,right_half)]
            left_half = tmp
        else :
            tmp = right_half
            right_half = left_half
            left_half = tmp
            
    
    
    
    firstIndex = lastIndex
    iteration += 1
    lastIndex = (iteration * 16)
    print("lastlastindex : " + str(lastIndex))
    print("elsecontrol")
    cipher.extend(left_half + right_half)
    
print(cipher)
print(len(cipher))

for i in range(0,len(cipher)):
    cipher[i] = alphabet[cipher[i]]

print("".join(cipher))