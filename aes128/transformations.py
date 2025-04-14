from .constants import s_box
from .helpers import xtime, mix_single_column

# 4. SubBytes
def sub_bytes(state):
    return [[s_box[byte] for byte in row] for row in state]

# 5. ShiftRows
def shift_rows(state):
    new_state = [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]
    return new_state

# 6. MixColumns Helper: GF(2^8) Multiplication
def xtime(a):
    return ((a << 1) ^ 0x1b) & 0xff if a & 0x80 else (a << 1)

def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    return a

# 7. MixColumns
def mix_columns(state):
    for i in range(4):
        col = [state[j][i] for j in range(4)]
        col = mix_single_column(col)
        for j in range(4):
            state[j][i] = col[j]
    return state

# 8. AddRoundKey
def add_round_key(state, round_key):
    return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]