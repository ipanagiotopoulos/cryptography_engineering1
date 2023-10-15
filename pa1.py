# Define your Bit_Material_Con, Coverting_KEY, Matrix_8x4, and MultiplicationKEYBitMatrix functions here
#coverting Bit_Material
def Bit_Material_Con(x):
    Decimal_Num=[]
    for i in range(len(x)):
                  
        decimal_value = int(x[i], 16)
        Decimal_Num.append(decimal_value+1) 

    return Decimal_Num

#Coverting KEY into Numeric List:
def Coverting_KEY(Key):
    numlist = [ord(x) - 65 for x in Key]                             # Make a list of numbers from letters.
    matrix  = [numlist[i:i+4] for i in range(0, 16, 4)]

    return matrix

#Coverting the Remain 8 bits of Bit Material to 8x4
def Matrix_8x4(x):
    Hexchar=x
    HexLIST=[]

    hxarray=[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
           [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1], [0,0,0,1],[0,0,1,0]]
    for i in Hexchar:

        row = hxarray[int(i,16)]
        HexLIST.append(row)

    return HexLIST

#Multiplication of KEY & Bit Matrix and their MUD 26
def MultiplicationKEYBitMatrix(KeyM,BitM):
    result=[]
    result = [[0 for _ in range(len(KeyM[0]))] for _ in range(len(BitM))]
    for i in range(len(BitM)):
   # iterate through columns of Y
        for j in range(len(KeyM[0])):
       # iterate through rows of Y
            for k in range(len(KeyM)):
                result[i][j] += (BitM[i][k] * KeyM[k][j] )
            result[i][j] = result[i][j] % 26

    return result

# Define your Bit_Material_Con, Coverting_KEY, Matrix_8x4, and MultiplicationKEYBitMatrix functions here

# Define the Feistel operation
def feistel(left_half, right_half, round_key, mult,RoundNum):
    new_left_half = [0] * 8
    new_right_half = [0] * 8
    
    # Apply the Feistel operation to each "letter"
    for i in range(8):
        if RoundNum<15:
            new_left_half[i] = (left_half[i] + mult * right_half[i] + round_key[i]) % 26
            new_right_half[i] = new_left_half[i]
            new_left_half[i]=right_half[i]
        else:
            new_left_half[i] = (left_half[i] + mult * right_half[i] + round_key[i]) % 26
            new_right_half[i] = right_half[i]

        
    return new_left_half, new_right_half

# Main Function:
Bit_Material = ""   #put bit material here

First16Bits = Bit_Material[0:16]
Last08Bits = Bit_Material[16:24]

Mult = Bit_Material_Con(First16Bits)

PlainText = "ITISNOTTOOTRICKY"
Key = "KEYSAREESSENTIAL"

KEYMatrix = Coverting_KEY(Key)

BitMatrix = Matrix_8x4(Last08Bits)

KeySchedule=MultiplicationKEYBitMatrix(KEYMatrix,BitMatrix)



# Initialize the left and right halves
left_half = [ord(char) - 65 for char in PlainText[:8]]
right_half = [ord(char) - 65 for char in PlainText[8:]]

for round_num in range(16):  
    round_key = [row[round_num % 4] for row in KeySchedule]


    left_half, right_half = feistel(left_half, right_half, round_key, Mult[round_num],round_num)

    # Output the input to each round
    print(f"Left & Right Side After Round {round_num}:")
    print("".join([chr(char + 65) for char in left_half]), "".join([chr(char + 65) for char in right_half]))

# The final left and right halves are your ciphertext
ciphertext = left_half + right_half

print("Ciphertext:", "".join([chr(char + 65) for char in ciphertext]))