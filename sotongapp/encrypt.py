from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path
import os, environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


def readPEM():
    h = open(env('PEM_FILE_NAME'), 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def get_encryptor():
    private_key = readPEM()
    public_key = private_key.public_key()
    return public_key.export_key()

def RSA_enc(code):
    public_key = get_encryptor()
    encryptor = PKCS1_OAEP.new(RSA.importKey(public_key))
    encrypted = encryptor.encrypt(code.encode())
    return encrypted

def RSA_dec(code):
    try:
        private_key = readPEM()
        decryptor = PKCS1_OAEP.new(private_key)
        decrypted = decryptor.decrypt(code)
    except:
        return 'X'
    return decrypted.decode()


# code = env('PEM_SECRET')
# ciphered = RSA_enc(code)
# print(RSA_dec(ciphered))
