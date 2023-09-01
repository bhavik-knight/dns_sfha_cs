import hashlib


def main():
    plain_text = str.strip(input("Plain text: "))
    print(f"SHA256 hash: {encode_sha256(plain=plain_text)}")
    print(f"MD5 hash: {encode_md5(plain=plain_text)}")


def encode_sha256(plain: str) -> str:
    encoded_plain = str.encode(plain)
    encoded = hashlib.sha256(encoded_plain)
    return encoded.hexdigest()


def encode_md5(plain: str) -> str:
    encoded_plain = str.encode(plain)
    encoded = hashlib.md5(encoded_plain)
    return encoded.hexdigest()


if __name__ == "__main__":
    main()
