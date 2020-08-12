import base64
import os
import string
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class PasswordManager:

    def __init__(self):
        self.data_name = "password_manager_data.dat"
        self.salt_name = "password_manager_salt.dat"
        self.first_run = self.check_if_first_run()

    def generate_key(self, provided_password):
        password = provided_password.encode()
        salt = self.salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    
    def check_correct_password(self, password):
        key = self.generate_key(password)
        with open(self.data_name, 'rb') as f:
            data = f.read()
        Fernet(key).decrypt(data)

    def decrypt(self, password):
        key = self.generate_key(password)
        with open(self.data_name, 'rb') as f:
            data = f.read()
        decrypted = Fernet(key).decrypt(data)
        with open(self.data_name, 'wb') as f:
            f.write(decrypted)

    def encrypt(self, password):
        key = self.generate_key(password)
        with open(self.data_name, 'rb') as f:
            data = f.read()
        os.remove(self.data_name)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(self.data_name, 'wb') as f:
            f.write(encrypted)
    
    def generate_files(self):
        open(self.data_name, "x")
        open(self.salt_name, "x")

    def check_if_first_run(self):
        try:
            open(self.data_name)
        except FileNotFoundError:
            return True
        else:
            return False

    def generate_salt(self):
        if self.first_run:
            self.salt = os.urandom(32)
            with open(self.salt_name, "wb") as f:
                f.write(self.salt)
        else:
            with open(self.salt_name, "rb") as f:
                salt = f.read()
            self.salt = salt

    def list_accounts(self, universal_password):
        self.decrypt(universal_password)
        with open(self.data_name, 'r') as f:
            lines = f.readlines()
        self.encrypt(universal_password)
        return lines

    def add_account(self, account_name, username, password, universal_password):
        account = dict(Account=account_name, Username=username, Password=password)
        self.decrypt(universal_password)
        with open(self.data_name, 'a') as f:
            f.write(str(account) + "\n")
        self.encrypt(universal_password)
    
    def generate_password(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3):
                break
        return password
    
    def load_QCombobox_items(self, universal_password):
        self.decrypt(universal_password)
        with open(self.data_name, 'r') as f:
            lines = f.readlines()
        empty = os.stat(self.data_name).st_size
        self.encrypt(universal_password)
        account_dict = {}
        if empty == 0:
            return account_dict
        if lines:
            for line in lines:
                convertdict = eval(line)
                string = ""
                count = 0
                for credential, value in convertdict.items():
                    count += 1
                    if count < 3:
                        string += f"{credential}: {value}\n"
                    else:
                        string += f"{credential}: {value}"
                if not account_dict:
                    account_dict[0] = string
                else:
                    account_dict[max(account_dict, key=int) + 1] = string
            return account_dict

    def remove_account(self, universal_password, index):
        self.decrypt(universal_password)
        with open(self.data_name, 'r+') as f:
            lines = f.readlines()
            f.truncate(0)
        lines.pop(index)
        for line in lines:
            write_line = eval(line)
            with open(self.data_name, 'a') as f:
                f.write(str(write_line) + "\n")
        self.encrypt(universal_password)