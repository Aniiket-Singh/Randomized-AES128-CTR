from aes128.encrypt import encrypt_block

input_text = "Example"
plaintext = input_text.encode().ljust(16, b'\x00')
input_key = "MySecretKey"
key = input_key.encode().ljust(16, b'\x00')

ciphertext = encrypt_block(plaintext, key)
print("Ciphertext:", ciphertext.hex())
