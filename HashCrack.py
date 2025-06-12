import hashlib  

def lerArquivo(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def hashList():
    hashes = []
    for palavra in lerArquivo("wordlist.txt"):
        hash_obj = hashlib.sha256(palavra.encode('utf-8'))
        hashes.append(hash_obj.hexdigest())
    return hashes

def comparaHashes(hashes,alvo):
    for hash in hashes:
        if hash == alvo:
            print("Hash encontrado na wordlist: ", hash)
    
print(hashList())

comparaHashes(hashes= hashList(),alvo= input("Digite a sua hash: "))