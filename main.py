import pk15
from Crypto.PublicKey import RSA
import base64

your_public_key = "" # should in base64
your_encrypt_msg = "" # should in base64




public_key = """-----BEGIN RSA PUBLIC KEY-----
{}
-----END RSA PUBLIC KEY-----""".format(your_public_key)
key = RSA.import_key(public_key)
sign = "{}".format(your_encrypt_msg)
sign_bytes = base64.b64decode(sign.encode())

print(pk15.new(key).decrypt(sign_bytes))