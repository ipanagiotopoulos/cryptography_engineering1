#Author Panagiotopoulos Ioannis
#Course Crypt Eng 1 - Tampere University
#Week 40 - Programming exercise 1


def string_converter(string):
    text_to_convert = [ char for char in  string]
    converted_string = ["0"] * len(text_to_convert)
    for char_index in range(0,len(string), 1):
        if ord(text_to_convert[char_index]) >=97 and ord(text_to_convert[char_index]) <= 97+26:
         converted_string[char_index] = chr(ord(text_to_convert[char_index])-26)
        else:
          converted_string[char_index] = text_to_convert[char_index]
    return converted_string

def numneric_operation(modified_string):
   text_to_numerify = [ char for char in  modified_string]
   result = [0] *len(text_to_numerify)
   for char_index in range(0,len(text_to_numerify), 1):
        if ord(text_to_numerify[char_index]) >=97 and ord(text_to_numerify[char_index]) <= 97+26:
         result[char_index] = ord(text_to_numerify[char_index]-97)
        else:
          result[char_index] = text_to_numerify[char_index]
   return result


def text_analysis(numerified_string):
   frequencies = [0]*26
   text_to_analyse = [char for char in numerified_string]
   for char_index in range(0,len(text_to_analyse), 1):
      if ord(text_to_analyse[char_index]) >=97 and ord(text_to_analyse[char_index]) <= 97+26:
         frequencies[ord(text_to_analyse[char_index])-97] +=1
   return frequencies

def present_stats(string, frequencies, start_index, last_index):
   start_index =  start_index % 26
   last_index  = last_index % 26
   print("Given string:", string)
   frequencies = frequencies[start_index:last_index]
   counter = 0
   for freq in range(0, len(frequencies), 1):
        print("Characher: "+chr(ord(97+counter))+" appears "+frequencies[freq]+" times")
        counter +=1


def affine_transformation(integer_one, integer_two, numerified_string):
   result = ["0"]*len(numerified_string)
   for index in range(0, len(numerified_string), 1):
      result[index] = chr((integer_one*numerified_string[index] +integer_two)%26)
   return result



def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def modinvert(a, m):
   if gcd(a, m) != 1:
      return None
   u1, u2, u3 = 1, 0, a
   v1, v2, v3 = 0, 1, m

   while v3 != 0:
      q = u3 // v3
      v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
   return u1 % m




def main():
    string_to_be_converted = ""

    while(string_to_be_converted == ""):
        string_to_be_converted = input("Give me the string to be converted\n")
        if string_to_be_converted == "":
            print("Please try again!\n")
    integer_one, integer_two = -1
    while( integer_one  < 0 or integer_one > 26 and integer_one == 13):
       integer_one = int(input("Give an integer 0-26, except for 13"))
    while( integer_two < 0 or integer_two > 26 and integer_two == 13):
       integer_two = int(input("Give an integer 0-26, except for 13"))
    #Code to be written here
    #
    #
    #


if __name__ == "__main__":
    main()


