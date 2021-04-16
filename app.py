import hashlib

hashchain = []
hashchainLength = 1000_0000
previousHash = ""
for i in range(hashchainLength):
    previousHash = hashlib.sha256(previousHash.encode("utf-8")).hexdigest()
    # hashchain.append(previousHash)
    # print(previousHash)
print("done")
