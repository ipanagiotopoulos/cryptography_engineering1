#Author Panagiotopoulos Ioannis
#Course Crypt Eng 1 - Tampere University
#Week 40 - Programming exercise 1
import sys
import time
import signal


PROG_ROUNDS = 4

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
        print(final_string)
        print(len(final_string))
        break
    break


if __name__ == "__main__":
    try:
        print("Press CTRL+C to stop \n")
        main()
    except KeyboardInterrupt:
        pass
    finally:
        signal.signal(signal.SIGINT, signal_handler)


