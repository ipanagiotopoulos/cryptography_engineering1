#Author Panagiotopoulos Ioannis
#Course Crypt Eng 1 - Tampere University
#Week 40 - Programming exercise 1

PROG1_EX_BIT_MATERIAL = 0xFC14E1BEAEB7F3DEFF2CD2A






def main():
   hex_input =""
   while True:
        try:
            hex_input = input("Give me a hex of length:8")
            hex_input = int(hex_input, 16)
            if(hex_input.bit_length < 64):
               break
            else:
                continue
        except:
            print("error while inputing hex_input")

if __name__ == "__main__":
    main()

