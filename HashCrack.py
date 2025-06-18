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

def gerarHash(palavra,tipo):
    hashObj = hashlib.new(tipo) ## Cria objeto da variável tipo
    hashObj.update(palavra.encode('utf-8')) 
    return hashObj.hexdigest() ## Retorna a hash da string

def encontrarPalavra(alvo):
    wordlist = lerArquivo("wordlist.txt")
    tipo = input("Insira o tipo de hash (ex: sha255, sha384) >")

    for palavra in wordlist:
        if gerarHash(palavra, tipo) == alvo:
            print("Hash encontrado na wordlist: ", palavra)
            return
    print("Hash nao encontrado na wordlist: ")

print(gerarHash('oi','sha256'))

encontrarPalavra(input("Insira seu hash alvo para ser consultado > "))

