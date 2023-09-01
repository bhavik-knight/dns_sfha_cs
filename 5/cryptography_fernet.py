import os
from pathlib import Path

from cryptography.fernet import Fernet


def main():
    plain = str.strip(input("Plain text: "))

    # generate and get the key
    generate_key()
    key = get_key()

    # instantiate the fetnet class using the key generated
    fernet_encryption = Fernet(key)

    # encrypt the message
    cipher = encrypt(plain, fernet_encryption)
    print(f"\nCipher text: {cipher}")

    # decrypt the message
    plain = decrypt(cipher, fernet_encryption)
    print(f"\nPlain text: {plain}")


def encrypt(plain: str, algorithm) -> str:
    encoded_plain = str.encode(plain)
    encoded = algorithm.encrypt(encoded_plain)
    return encoded.decode()


def decrypt(cipher: str, algorithm) -> str:
    encoded_cipher = str.encode(cipher)
    decoded = algorithm.decrypt(encoded_cipher)
    return decoded.decode()


def get_key():
    file_path = Path(__file__).parent.joinpath("keys/fernet_key.pem")

    # read the file
    with open(file_path, "rb") as file:
        key = file.readline()
    return key


def generate_key():
    file_path = Path(__file__).parent.joinpath("keys")
    try:
        os.mkdir(file_path)
    except FileExistsError:
        pass

    key_file_path = file_path.joinpath("fernet_key.pem")
    key = Fernet.generate_key()

    # write the file
    with open(key_file_path, "wb") as file:
        file.writelines([key])
    return None


if __name__ == "__main__":
    main()
