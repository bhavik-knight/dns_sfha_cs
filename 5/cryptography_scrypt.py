from random import choice
from string import ascii_letters, digits

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def main():
    new_password = str.strip(input("Set a new password: "))

    # instantiate the object
    pwd = Password()

    # get the salt for the encryption
    salt = pwd.get_salt()
    # print(f"Salt: {salt}")

    # set the password using this salt
    pwd.set_password(new_password, salt)

    # ask for the pwd cofirmation
    confirm_pwd = str.strip(input("Confirm the password: "))
    if pwd.check_password(confirm_pwd):
        print("Passwords match!")
    else:
        print("Passwords didn't match :(")


class Password:
    def __init__(self, length: int = 10):
        self.set_salt(length)

    def get_salt(self):
        return self.__salt

    def set_salt(self, length):
        # generate random salt from ascii letters and digits of length <length>
        new_salt = "".join(map(lambda _: choice(ascii_letters + digits), range(length)))
        self.__salt = new_salt.encode()

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str, salt: bytes) -> str:
        encoded_pwd = password.encode()
        generate_hash = Scrypt(salt=salt, length=64, n=2048, r=8, p=1)
        self.__password = generate_hash.derive(encoded_pwd)

    def check_password(self, password: str) -> bool:
        encoded_pwd = password.encode()
        generated_hash = Scrypt(salt=self.get_salt(), length=64, n=2048, r=8, p=1)
        try:
            generated_hash.verify(encoded_pwd, self.get_password())
        except Exception:
            return False
        else:
            return True


if __name__ == "__main__":
    main()
