#Author Panagiotopoulos Ioannis
#Course Crypt Eng 1 - Tampere University
#Week 40 - Programming exercise 1
import signal
import sys
import time
import numpy as np


#static variables for feistel
PROG1_EX_BIT_MATERIAL = 0xFC14E1BEAEB7F3DEFF2CD2A
MATRIX_COLUMNS_NUMBER = 8
MATRIX_ROWS_NUMBER = 4
DEFAULT_MODULO = 26

#hex related conversions
HEX_ALLOWED_CHARS = [ "0", "1", "2", "3",
                      "4", "5", "6", "7",
                      "8", "9", "A", "B",
                      "C", "D", "E", "F"
                    ]

HEX_ARRAY = [   [0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],  #[0,O] .... [0,4]
                [0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
                [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],
                [1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1],
            ]
ENGLISH_ALPH_CHARS = [ "A", "B", "C", "D",
                      "E", "F", "G", "H",
                      "I", "J", "K", "M",
                      "N", "O", "P", "Q"
                    ]

NUM_LIST = [ord(x) - 65 for x in ENGLISH_ALPH_CHARS]
ENGLISH_ALPH_MATRIX = [NUM_LIST[i:i+4] for i in range(0, 16, 4)]

def hex_checker(hex_input):
    for char_index in range(0, len(hex_input), 1):
        if not(hex_input[char_index] in HEX_ALLOWED_CHARS ):
            print("Non allowed char in index:", char_index)
            print("Non allowed char", hex_input[char_index])
            return False
    return True


def string_converter(string):
    text_to_convert = [ char for char in  string]
    converted_string = ["0"] * len(text_to_convert)
    for char_index in range(0,len(string), 1):
        if ord(text_to_convert[char_index]) >=97 and ord(text_to_convert[char_index]) <= 97+25:
         converted_string[char_index] = chr(ord(text_to_convert[char_index])-32)
        else:
          converted_string[char_index] = text_to_convert[char_index]
    return "".join(converted_string)


def signal_handler(sig, frame):
    print('SIGINT signal received....')
    time.sleep(2)
    print('exit!')
    sys.exit(0)


def explode_hex_bin_matr(hex_string_array):
    converted_matrix =  [[0]*MATRIX_ROWS_NUMBER]*MATRIX_COLUMNS_NUMBER
    counter = 0
    for char_index in range(0,len(hex_string_array), 1):
        found_allowed_hex_index = HEX_ALLOWED_CHARS.index(hex_string_array[char_index])
        converted_matrix[char_index] = HEX_ARRAY[found_allowed_hex_index]
        counter += 1
    return converted_matrix

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])

def main():
   hex_input =""
   hex_input_array =[]
   while True:
        try:
            hex_input = input("Give me a hexadecimal number of length 8: ")
            if len(hex_input) !=8:
                print("hex_input has to be an 8 digit length hexadecimal but the length is "+str(len(hex_input))+"\n")
                continue
            hex_input_array = string_converter(hex_input)
            hex_input = "".join(hex_input_array)
            if hex_checker(hex_input_array):
                break
            else:
                continue
        except KeyError:
            print(KeyError.with_traceback)
   result = explode_hex_bin_matr(hex_input_array)
   print("Hex input array")
   print_matrix(result)
   print("English alph matrix")
   print_matrix(ENGLISH_ALPH_MATRIX)
   print("mult two arrays MOD 26", np.dot(result, ENGLISH_ALPH_MATRIX)%DEFAULT_MODULO)
   #new_matrix = np.dot(hex_input_array, ENGLISH_ALPH_MATRIX)
   #print("Result of multiplication", new_matrix)




if __name__ == "__main__":
    try:
        print("Press CTRL+C to stop \n")
        main()
    except KeyboardInterrupt:
        pass
    finally:
        signal.signal(signal.SIGINT, signal_handler)


