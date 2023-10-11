BIT_MATERIAL_2 = 0xf81f89e91556f877f20fde38
BIT_MATERIAL = 0x000000000000000000000000
PLAINTEXT = "ITISNOTTOOTRICKY"
KEY = "KEYSAREESSENTIAL"
ROUNDS = 16
MODULO = 26

mappings = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

reverse_mappings = dict(zip(mappings.values(), mappings.keys()))


def string_to_ints(string):
    return [ord(x) - 65 for x in string]


def ints_to_string(ints):
    char_list = [(reverse_mappings[ints[i]]) for i in range(len(ints))]
    return ''.join(char_list)


def hex_to_bin(hex):
    matrix = []
    for char in hex:
        binary = bin(int(char, 16))[2:]
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


hex_digits = hex(BIT_MATERIAL)[2:]
first_16 = hex_digits[:16]
last_8 = hex_digits[16:24]

if __name__ == "__main__":
    Mult = [int(first_16[i], 16) +
            1 for i in range(len(first_16))]
    print("Mult:")
    print(Mult)

    key_matrix = [KEY[i:i+4] for i in range(0, len(KEY), 4)]
    print("Key matrix:")
    print_matrix(key_matrix)


    key_nums = string_to_ints(KEY)
    key_num_matrix = [key_nums[i:i+4] for i in range(0, 16, 4)]
    print("Key number matrix:")
    print_matrix(key_num_matrix)

    last_8_matrix = hex_to_bin(last_8)
    print("Matrix of the bit material's last 8 digits:")
    print_matrix(last_8_matrix)

    key_schedule_matrix = matrix_mult_mod_26(last_8_matrix, key_num_matrix)
    print("Key schedule matrix:")
    print_matrix(key_schedule_matrix)

    block = string_to_ints(PLAINTEXT)
    for r in range(ROUNDS):
        print(f"Input to round {r}:")
        print(ints_to_string(block))
        i = r % 4

        round_key_values = [row[i] for row in key_schedule_matrix]
        print("Roundkey:")
        print(round_key_values)

        left_half = block[0:8]
        right_half = block[8:16]
        block = []

        if r != ROUNDS-1:
            for j in range(len(right_half)):
                block.append(right_half[j])

        new_left_half = [(Mult[r] * right_half[i] +
                          round_key_values[i]) % MODULO for i in range(len(left_half))]

        for j in range(len(new_left_half)):
            block.append(new_left_half[j])

        if r == ROUNDS-1:
            for j in range(len(right_half)):
                block.append(right_half[j])
    print("Result:")
    print(ints_to_string(block))