import hashlib

def criar_hash_senha(senha):
  
    hash_obj = hashlib.sha256()

    hash_obj.update(senha.encode('utf-8'))

    senha_hash = hash_obj.hexdigest()

    return senha_hash


senha = input("Digite a senha: ")

senha_hash = criar_hash_senha(senha)

print("A senha em hash é:",senha_hash)