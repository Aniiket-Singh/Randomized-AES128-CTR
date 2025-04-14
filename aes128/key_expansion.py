from .constants import s_box, r_con

# 3. Key Expansion (implements RotWord and SubWord as before)
def key_expansion(key):
    key_columns = [list(key[i:i+4]) for i in range(0, 16, 4)]
    i = 4
    while len(key_columns) < 44:
        temp = key_columns[-1].copy()
        if i % 4 == 0:
            # RotWord: rotate left by one byte
            temp = temp[1:] + temp[:1]
            # SubWord: apply S-box substitution
            temp = [s_box[b] for b in temp]
            # Apply Rcon to the first byte
            temp[0] ^= r_con[i // 4]
        word = [a ^ b for a, b in zip(key_columns[-4], temp)]
        key_columns.append(word)
        i += 1
    round_keys = [key_columns[4*i:4*(i+1)] for i in range(11)]
    # Transpose each round key to convert from row-major to column-major format.
    return [[list(col) for col in zip(*round)] for round in round_keys]