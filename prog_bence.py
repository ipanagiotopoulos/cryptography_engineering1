Mult = [int(first_16[i], 16) + 1 for i in range(len(first_16))]


def hex_to_bin(hex):
    matrix = []
    for char in hex:
        binary = bin(int(char, 16))[2:]
        binary = binary.zfill(4)
        binary_list = [int(bit) for bit in binary]
        matrix.append(binary_list)
    return matrix


def matrix_mult_mod_26(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Can't multiply the two matrices.")

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] % MODULO
    return result


ROUNDS = 14

def main():
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
