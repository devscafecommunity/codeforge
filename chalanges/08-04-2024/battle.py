import random

class Personagem:
    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp_maximo = hp
        self.hp_atual = hp
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = []

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.hp_atual = max(0, alvo.hp_atual - dano)
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")

    def usar_habilidade(self, alvo, habilidade_index):
        if habilidade_index < len(self.habilidades):
            habilidade = self.habilidades[habilidade_index]
            habilidade.executar(self, alvo)
        else:
            print("Habilidade inválida!")

    def esta_vivo(self):
        return self.hp_atual > 0

class Habilidade:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def executar(self, caster, alvo):
        dano_total = max(0, self.dano - alvo.defesa)
        alvo.hp_atual = max(0, alvo.hp_atual - dano_total)
        print(f"{caster.nome} usa {self.nome} em {alvo.nome} e causa {dano_total} de dano.")

class AtaqueDuplo(Habilidade):
    def __init__(self):
        super().__init__("Ataque Duplo", 15)

class DefesaReforçada(Habilidade):
    def __init__(self):
        super().__init__("Defesa Reforçada", 0)

class Inimigo(Personagem):
    def __init__(self, nome, hp, ataque, defesa):
        super().__init__(nome, hp, ataque, defesa)

    def tomar_decisao(self, heroi):
        acao = random.choice(["atacar", "defender", "habilidade"])
        if acao == "atacar":
            self.atacar(heroi)
        elif acao == "defender":
            print(f"{self.nome} decide se proteger!")
        elif self.habilidades:  # Verifica se o inimigo tem habilidades
            habilidade_index = random.randint(0, len(self.habilidades) - 1)
            self.usar_habilidade(heroi, habilidade_index)
        else:
            print(f"{self.nome} tenta atacar, mas não tem habilidades!")

def batalha(heroi, inimigo):
    print("Começa a batalha!")
    turno = 1
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print(f"Turno {turno}:")
        if turno % 2 != 0:  # Turno do herói
            print(f"Seu HP: {heroi.hp_atual}/{heroi.hp_maximo}")
            print(f"{inimigo.nome} HP: {inimigo.hp_atual}/{inimigo.hp_maximo}")
            print("Escolha uma ação:")
            print("1. Atacar")
            print("2. Usar Habilidade")
            escolha = input(">> ")
            if escolha == "1":
                heroi.atacar(inimigo)
            elif escolha == "2":
                print("Escolha a habilidade:")
                for i, habilidade in enumerate(heroi.habilidades):
                    print(f"{i+1}. {habilidade.nome}")
                habilidade_escolhida = int(input(">> ")) - 1
                heroi.usar_habilidade(inimigo, habilidade_escolhida)
            else:
                print("Escolha inválida!")
        else:  # Turno do inimigo
            inimigo.tomar_decisao(heroi)
        turno += 1

    if heroi.esta_vivo():
        print("Você venceu!")
    else:
        print("Você foi derrotado!")

# Exemplo de uso
heroi = Personagem("Herói", 100, 20, 10)
heroi.habilidades.append(AtaqueDuplo())
heroi.habilidades.append(DefesaReforçada())
inimigo = Inimigo("Goblin", 50, 15, 5)
batalha(heroi, inimigo)
