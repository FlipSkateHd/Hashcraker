import hashlib

##  COMPARAÇÃO DE OBJETO DE HASH COM VALOR DE HASH

objeto_hash = hashlib.sha256(b"senhasecreta")
print(objeto_hash)
## Esse aqui retorna o ponteiro da memória para o objeto desse hash que foi feito

## Ao pegar o objeto e usar o "digest", obtém o hash calculado em hexadecimal, normalmente usado em verificações
hash_legal = objeto_hash.hexdigest()
print(hash_legal)
