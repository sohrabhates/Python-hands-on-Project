from cryptography.fernet import Fernet
import os


# =========================================================
# ENCRYPTION KEY
# =========================================================

def write_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as file:
        return file.read()


# Create key only if it doesn't already exist
if not os.path.exists("key.key"):
    write_key()


key = load_key()
fer = Fernet(key)


# =========================================================
# ADD PASSWORD
# =========================================================

def add(name, pwd):

    encrypted_password = fer.encrypt(
        pwd.encode()
    ).decode()

    with open("passwords.txt", "a") as f:
        f.write(
            name + "|" + encrypted_password + "\n"
        )


# =========================================================
# VIEW PASSWORDS
# =========================================================

def view():

    passwords = []

    try:

        with open("passwords.txt", "r") as f:

            for line in f:

                data = line.strip()

                if "|" not in data:
                    continue

                user, encrypted_password = data.split("|", 1)

                try:

                    password = fer.decrypt(
                        encrypted_password.encode()
                    ).decode()

                    passwords.append(
                        (user, password)
                    )

                except Exception:

                    continue

    except FileNotFoundError:

        pass

    return passwords