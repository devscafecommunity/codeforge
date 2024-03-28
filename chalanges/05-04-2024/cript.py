def criptografar_mensagem(mensagem, chave):
    mensagem_criptografada = ""
    for letra in mensagem:
        if letra.isalpha():
            codigo = ord(letra) + chave
            if letra.islower():
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            elif letra.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            mensagem_criptografada += chr(codigo)
        else:
            mensagem_criptografada += letra
    return mensagem_criptografada

mensagem = "O segredo esta na montanha proibida"
chave = 3
mensagem_criptografada = criptografar_mensagem(mensagem, chave)
print("Mensagem criptografada:", mensagem_criptografada)

def descriptografar_mensagem(mensagem_criptografada, chave):
    mensagem_descriptografada = ""
    for letra in mensagem_criptografada:
        if letra.isalpha():
            codigo = ord(letra) - chave
            if letra.islower():
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            elif letra.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            mensagem_descriptografada += chr(codigo)
        else:
            mensagem_descriptografada += letra
    return mensagem_descriptografada

mensagem = "O segredo esta na montanha proibida"
chave = 3
mensagem_criptografada = criptografar_mensagem(mensagem, chave)
print("Mensagem criptografada:", mensagem_criptografada)

mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, chave)
print("Mensagem descriptografada:", mensagem_descriptografada)
