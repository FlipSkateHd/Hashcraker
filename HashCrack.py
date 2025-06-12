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
            return
    print("Hash nao encontrado na wordlist: ")


comparaHashes(hashes= hashList(),alvo= input("Digite a sua hash: "))


## futura  melhoria:
# def encontrar_palavra(wordlist, hash_alvo, tipo="sha256"):
#    for palavra in wordlist:
#        if gerar_hash(palavra, tipo) == hash_alvo:
#            print(f"✅ Palavra encontrada: '{palavra}'")
#            return