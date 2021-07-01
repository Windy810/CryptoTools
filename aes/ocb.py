import json
from base64 import b64encode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

header = b"header"
data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OCB)
cipher.update(header)
ciphertext, tag = cipher.encrypt_and_digest(data)

json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
json_v = [b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag)]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)
# from ocb.aes import AES
# from ocb import OCB

# aes = AES(128)
# print(aes)
# ocb = OCB(aes)
# print(ocb)