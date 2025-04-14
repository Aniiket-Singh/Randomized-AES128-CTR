from .helpers import bytes_to_matrix, matrix_to_bytes
from .key_expansion import key_expansion
from .transformations import sub_bytes, shift_rows, mix_columns, add_round_key

def encrypt_block(plaintext, key):
    state = bytes_to_matrix(plaintext)
    round_keys = key_expansion(key)

    state = add_round_key(state, round_keys[0])

    for i in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[i])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[10])

    return matrix_to_bytes(state)
