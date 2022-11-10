import requests
import hashlib
import sys

file_name = sys.argv[1]
print(file_name)

file = open(sys.argv[1]).read().split('\n')
for passw in file:
    if passw != '---':
        encode_passw = str.encode(passw)
        pwn_pass = hashlib.sha1(encode_passw)
        phHash = pwn_pass.hexdigest()
        hash_five = phHash[0:5]
        hash_all = phHash[5:]
        requset = requests.get('https://api.pwnedpasswords.com/range/' + hash_five).text
        res = requset.lower().find(hash_all)
        if res == -1:
            print(passw + ': NOT LEAKED')
        else:
            print(passw + ' : LEAKED!')