PROG1_EX_BIT_MATERIAL = 0xFC14E1BEAEB7F3DEFF2CD2A
TEXT_PLAINTEXT = "ITISNOTTOOTRICKY"
EXERCISE_KEY = "KEYSAREESSENTIAL"
FEISTEL_ROUNDS = 16
FEISTEL_MODULO = 26

def alpha_dict_mappings(alphabet_list):
    for char in range(0, len(alphabet_list), 1):
        print(char)

ALPHABETICAL_CHARACHTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
APLHABET_LIST = [char for char in ALPHABETICAL_CHARACHTERS]
ALPHA_DICT_MAPPINGS = alpha_dict_mappings(APLHABET_LIST)




def integers_to_string(integers):
    char_list = [(ALPHA_DICT_MAPPINGS[integers[i]]) for i in range(len(integers))]
    return ''.join(char_list)

def strings_to_integers(string):
    return [ord(char) - 65 for char in string]

def hexadcimal_to_binary(hexadecimal):
    matrix = []
    for hex in hexadecimal:
        binary = bin(int(hex, 16))[2:]
        binary = binary.zfill(4)
        binary_list = [int(bit) for bit in binary]
        matrix.append(binary_list)
    return matrix


def string_matrix_to_num_matrix(string_matrix):
    num_matrix = []
    for i in range(0, len(string_matrix)):
        row = []
        for j in range(0, len(string_matrix[i])):
            row.append(mappings[string_matrix[i][j]])
        num_matrix.append(row)
    return num_matrix


def matrix_mult_mod_26(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Can't multiply the two matrices.")

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]  # _ is tmp variable

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] % MODULO
    return result


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


hex_digits = hex(PROG1_EX_BIT_MATERIAL)[2:]
first_16 = hex_digits[:16]
last_8 = hex_digits[16:24]





def main():


if __name__ == "__main__":
    main()







