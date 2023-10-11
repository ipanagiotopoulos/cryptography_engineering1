#Author Panagiotopoulos Ioannis
#Course Crypt Eng 1 - Tampere University
#Week 40 - Programming exercise 1
import sys
import time
import signal
from copy import deepcopy


PROG_ROUNDS = 4
MID_POSITION = 8

def signal_handler(sig, frame):
    print('SIGINT signal received....')
    time.sleep(2)
    print('exit!')
    sys.exit(0)

def string_converter(string):
    text_to_convert = [ char for char in  string]
    converted_string = []
    for char_index in range(0,len(string), 1):
        if ord(text_to_convert[char_index]) >=97 and ord(text_to_convert[char_index]) <= 97+25:
         converted_string.append(chr(ord(text_to_convert[char_index])-32))
        elif ord(text_to_convert[char_index]) >=65 and ord(text_to_convert[char_index]) <= 65+25:
            converted_string.append(text_to_convert[char_index])
    return "".join(converted_string)


def pad_string(string_to_pad):
    padded_string = [char for char in string_to_pad]
    remainder = 16 - (len(padded_string) % 16)
    for i in range(0, remainder, 1):
        padded_string.append("0")
    return padded_string




def split_array(array):
    len_array = len(array)
    part = int(len_array /16)
    result_array = [["0"]*16]*part
    flag = False
    for index_1 in range(0, part, 1):
        if flag:
            break
        for index_2 in range(0, 16, 1):
            final_index = index_1*16+index_2
            if final_index >= len_array:
                flag =True
            result_array[index_1][index_2] = array[final_index]
    return result_array

def feistel(double_dim_array):
    len_array = len(double_dim_array)
    part = int(len_array /16)
    ciphers = [[0]*16]*part
    for round in range(PROG_ROUNDS):
        for array_index in range(0, len(double_dim_array),1):
            right_half = double_dim_array[array_index][:8]
            print("typeeee", type(right_half[0]))
            left_half = double_dim_array[array_index][8:16]
            if round != PROG_ROUNDS -1:
                tmp = deepcopy(right_half)
                right_half = [(x+round*y)%26 for x,y in zip(left_half,right_half)]
                left_half = deepcopy(tmp)
            else:
                right_half = [(x+round*y)%26 for x,y in zip(left_half,right_half)]
            ciphers[array_index].extend(left_half + right_half)
    return ciphers







def main():
    while True:
        input_string  = input("Give me a string with a length multiple of 16:")
        final_string = string_converter(input_string)
        print("final string", final_string)
        if(len(final_string) == 0):
            print("Charachters from A-Z allowed or a-z")
            continue
        if(not(len(final_string)%16 == 0)):
            final_string = pad_string(final_string)
            break
        break
    splitted_array = split_array(final_string)
    for array_index in range(0, len(splitted_array), 1):
        splitted_array[array_index] = [ord(x) - 65 for x in splitted_array[array_index]]
    print("Splitted", splitted_array)
    print("Splitted Array size", len(splitted_array))
    ciphers = feistel(splitted_array)
    print("Ciphers", ciphers)


if __name__ == "__main__":
    try:
        print("Press CTRL+C to stop \n")
        main()
    except KeyboardInterrupt:
        pass
    finally:
        signal.signal(signal.SIGINT, signal_handler)


