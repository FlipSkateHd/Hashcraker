import sys 

import hashlib  

def ler_arquivo(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

hashes = []
Buffer = 65536
for palavra in ler_arquivo("wordlist.txt"):
    hashes.append(hashlib.sha256(palavra))

print(hashes)