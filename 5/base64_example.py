import base64


def main():
    plain_text = str.strip(input("Plain text: "))
    base64_encode = encode_base64(plain=plain_text)
    print(f"Cipher text: {base64_encode}")

    base64_decode = decode_base64(cipher=base64_encode)
    print(f"Plain text: {base64_decode}")
    return None


def encode_base64(plain: str) -> str:
    encode_plain = plain.encode()
    encoded = base64.b64encode(encode_plain)
    return encoded.decode()


def decode_base64(cipher: str) -> str:
    encode_cipher = cipher.encode()
    encoded = base64.b64decode(encode_cipher)
    return encoded.decode()


if __name__ == "__main__":
    main()
