from aes128 import encrypt_block, prepare_input, prepare_key, xor_bytes, int_to_bytes
import os

block_size = 16
ciphertext = b""
counter = 0
nonce = os.urandom(8)

input_text = "1234567890123456789012"  
input_key = "MySecretKey"  

plaintext = prepare_input(input_text)
key = prepare_key(input_key)

for i in range(0, len(plaintext), block_size):
    block = plaintext[i:i+block_size]
    counter_block = nonce + int_to_bytes(counter, 16 - len(nonce))
    keystream = encrypt_block(counter_block, key)
    ciphertext += xor_bytes(block, keystream[:len(block)])
    counter += 1

# ciphertext = encrypt_block(plaintext, key)
print("Ciphertext:", ciphertext.hex())