import copy
import numpy as np
hexBitMaterial = 0xf81f89e91556f877f20fde38
key = "KEYSAREESSENTIAL"
text = "ITISNOTTOOTRICKY"
round = 16

bitMat = "111011101100001100100110000010010000111001111101001000100010110001110011100101000010000011110100"
init = 0
byte = []
bytesMaterial = []
while True:
    if (init < len(bitMat)):
        for i in range (init,init + 4):
            #print(i)
            bit = bitMat[i]
            byte.append(int(bit))
            #print(byte)
        init = init+4
        temp = copy.deepcopy(byte)
        bytesMaterial.append(temp)
        byte.clear()
    else:
        break
    
firstSixteenDigit = bytesMaterial[:16]

print(firstSixteenDigit)


mult = []

for i in range(len(firstSixteenDigit)):
    
    multip = 4 #3
    index = 0 #1
    result = 0
    
    while index < len(firstSixteenDigit[i]):
        if (firstSixteenDigit[i][index] == 1):
            result += pow(2,4-(index+1))
            index += 1
        else: 
            index += 1
    mult.append(result)

print(mult)

for i in range(0, len(mult)):
    mult[i] = mult[i] + 1

print(mult)


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listAlphabet = list(alphabet)


newList = []

for i in key:
    newList.append(listAlphabet.index(i))

#"".join(newList)
print(newList)

keyMatrix = []

keyMatrix.append(newList[0:4])
keyMatrix.append(newList[4:8])
keyMatrix.append(newList[8:12])
keyMatrix.append(newList[12:16])


print("Key matrix : ")
for i in keyMatrix:
    print(i)

following8Digits = bytesMaterial[16:]
print("following 8")

for i in following8Digits:
    print(i)

multiplicationMatrix = []














keyMatrixNumpy = np.array(keyMatrix)
following8DigitsNumpy = np.array(following8Digits)
print("-------------------------")
print(keyMatrixNumpy)
print(following8DigitsNumpy)

if len(following8DigitsNumpy[0]) != len(keyMatrixNumpy):
    raise ValueError("Can't multiply the two matrices.")

result = [[0] * len(keyMatrixNumpy[0]) for _ in range(len(following8DigitsNumpy))]  # _ is tmp variable

for i in range(len(following8DigitsNumpy)):
    for j in range(len(keyMatrixNumpy[0])):
        for k in range(len(keyMatrixNumpy)):
            result[i][j] += following8DigitsNumpy[i][k] * keyMatrixNumpy[k][j] % 26

keyScheduleMatrix = result



#Feistel

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listAlphabet = list(alphabet)


block = []

for i in text:
    block.append(listAlphabet.index(i))

print("block : ")
print(block)

for r in range(round):
    b = r % 4
    print("i = " + str(i))
    roundKeyValues = [row[b] for row in keyScheduleMatrix]

    leftHalf = block[0:8]
    rightHalf = block[8:16]
    print("right half : ")
    print(rightHalf)
    print("left half : ")
    print(leftHalf)
    block = []
    if r != round-1:
        for j in range(len(rightHalf)):
            block.append(rightHalf[j])

    new_left_half = [(mult[r] * rightHalf[i] +
                        roundKeyValues[i]) % 26 for i in range(len(leftHalf))]

    for j in range(len(new_left_half)):
        block.append(new_left_half[j])

    if r == round-1:
        for j in range(len(rightHalf)):
            block.append(rightHalf[j])
    
    st = []
    for i in range(len(block)):
        st.append(alphabet[block[i]])
    print("".join(st))





