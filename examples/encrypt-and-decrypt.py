from cryptostream import CryptoStream
import time

encryptor = CryptoStream()
encryptor.add_recipient("other company", open("other company.pub").read(), '127.0.0.1:8554', private_key = open("other company.priv").read())
encryptor.add_recipient("sitebots", open("sitebots.pub").read(), '127.0.0.1:8555', private_key = open("sitebots.priv"))
encryptor.encrypt(3*'a' + 17*'b')
encryptor.encrypt(7*'c' + 7*'d')

time.sleep(1)

bdata = open("sitebots.bin", "rb").read()
data = encryptor.decrypt(bdata)
print(data)

bdata = open("oc.bin", "rb").read()
data = encryptor.decrypt(bdata, 1)
print(data)
