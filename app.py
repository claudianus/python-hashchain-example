import hashlib
import secrets

hashchain = []
hashchainLength = 1000_0000
previousHash = secrets.token_hex(1024) # generate 1024bytes random seed
for i in range(hashchainLength):
    previousHash = hashlib.sha256(previousHash.encode("utf-8")).hexdigest()
    # hashchain.append(previousHash)
    # print(previousHash)
print("done")
