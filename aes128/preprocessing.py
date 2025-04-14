def prepare_input(text: str) -> bytes:
    encoded = text.encode()
    # if len(encoded) > 16:
    #     raise ValueError("Plaintext length exceeds 16 bytes (128 bits).")
    return encoded.ljust(16, b'\x00')

def prepare_key(key: str) -> bytes:
    encoded = key.encode()
    if len(encoded) > 16:
        raise ValueError("Key length exceeds 16 bytes (128 bits).")
    return encoded.ljust(16, b'\x00')
