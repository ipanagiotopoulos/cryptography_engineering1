def string_converter(string):
    text_to_convert = [ char for char in  string]
    converted_string = ["0"] * len(text_to_convert)
    for char_index in range(0,len(string), 1):
        if ord(text_to_convert[char_index]) >=97 and ord(text_to_convert[char_index]) <= 97+25:
         converted_string[char_index] = chr(ord(text_to_convert[char_index])-32)
        else:
          converted_string[char_index] = text_to_convert[char_index]
    return converted_string



def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alphabet_list = [char for char in alphabet]

    inp = input("Enter Text : ")
    new_inp = string_converter(inp)
    print("Input", new_inp)
    rounds = int(input("rounds : "))
    new_list_input = [char for char in new_inp]

    for char_index in range(0, len(new_list_input), 1):
        if (new_list_input[char_index]):
            new_list_input.append(alphabet_list.index(new_list_input[char_index]))
        else:
            new_list_input.append(new_list_input[char_index])

    flag = 0

    while flag!=1:
       if(len(new_list_input) % 16 !=0): #if length is not 16 append 0s
          new_list_input.append(0)
       else:
          flag=1

    iteration = 0
    first_index = 1
    last_index = (iteration*16)
    cipher_text = []
    cipher_count =0
    length = len(new_list_input)
    area = []
    while True:
        if(last_index >= length):
            print("control")
            break
        mid_list_position = int((last_index - first_index / 4))

        area = new_list_input[first_index:last_index]

        first_index_area = 0
        #lastIndexArea = len(area) - 1
        mid_area_index = int(len(area) / 2)
        left_half = area[first_index_area:mid_area_index]
        right_half = area[mid_area_index:len(area)]

        for round in range(0, rounds):
            #Debug
            print("Debug ================")
            print("left half : " + str(left_half))
            print("right half : " + str(right_half))
            print("Debug ================")
            #Debug

            if (round != rounds - 1):
                tmp = right_half
                right_half = [(x+rounds*y)%26 for x,y in zip(left_half,right_half)]
                left_half = tmp
            else :
                tmp = right_half
                right_half = left_half
                left_half = tmp
        first_index = last_index
        iteration += 1
        last_index = (iteration * 16)
        print("Debug==========")
        print("last index : " + str(last_index))
        print("elsecontrol")
        print("Debug==========")
        cipher_text.extend(left_half + right_half)

    print("Cipher text:", cipher_text)
    print("Length of cipher text",len(cipher_text))
    for i in range(0,len(cipher_text)):
        cipher_text[i] = alphabet[cipher_text[i]]
    print("result:")
    print("".join(cipher_text))


if __name__ == "__main__":
    main()





