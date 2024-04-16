import random
import noise

class Mapa:
    def __init__(self, largura, altura, seed=None):
        self.largura = largura
        self.altura = altura
        self.seed = seed
        if seed:
            random.seed(seed)
            self.noise_seed = random.randint(0, 1000)  # Seed para o Perlin Noise
        else:
            self.seed = random.getrandbits(32)  # Se nenhuma seed for fornecida, gera uma aleatória de 32 bits
            random.seed(self.seed)
            self.noise_seed = random.randint(0, 1000)  # Seed para o Perlin Noise
        self.mapa = [['' for _ in range(largura)] for _ in range(altura)]
        self.biomas = {
            "🌳": "Floresta 🌳",
            "⛰️": "Montanha ⛰️",
            "🏜️": "Deserto 🏜️",
            "🌾": "Planície 🌾",
            "🌊": "Rio 🌊",
            "❄️": "Tundra ❄️",
            "🌴": "Selva 🌴",
            "🌲": "Taiga 🌲",
            "🌿": "Savana 🌿",
            "🏞️": "Lago 🏞️",
            "🌋": "Vulcão 🌋",
            # Adicione mais biomas aqui conforme necessário
        }

    def calcular_umidade(self):
        umidade = [[0 for _ in range(self.largura)] for _ in range(self.altura)]
        for y in range(self.altura):
            for x in range(self.largura):
                for dy in range(-5, 6):
                    for dx in range(-5, 6):
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < self.largura and 0 <= ny < self.altura:
                            if self.mapa[ny][nx] == "🌊" or self.mapa[ny][nx] == "🏞️":
                                umidade[y][x] += 1
        return umidade

    def gerar_terreno(self):
        umidade = self.calcular_umidade()
        for y in range(self.altura):
            for x in range(self.largura):
                noise_val = noise.pnoise2(x / 10, y / 10, octaves=6, persistence=0.5, lacunarity=2.0, repeatx=self.largura, repeaty=self.altura, base=self.noise_seed)
                umidade_val = umidade[y][x]
                if umidade_val < 5:
                    if noise_val < 0.2:
                        self.mapa[y][x] = "⛰️"
                    elif noise_val < 0.3:
                        self.mapa[y][x] = "🌳"
                    elif noise_val < 0.35:
                        self.mapa[y][x] = "🏜️"
                    else:
                        self.mapa[y][x] = "🌾"
                elif umidade_val < 15:
                    if noise_val < 0.2:
                        self.mapa[y][x] = "⛰️"
                    elif noise_val < 0.4:
                        self.mapa[y][x] = "🌳"
                    elif noise_val < 0.6:
                        self.mapa[y][x] = "🏜️"
                    else:
                        self.mapa[y][x] = "🌾"
                else:
                    if noise_val < 0.2:
                        self.mapa[y][x] = "⛰️"
                    elif noise_val < 0.4:
                        self.mapa[y][x] = "🌳"
                    elif noise_val < 0.7:
                        self.mapa[y][x] = "🏜️"
                    else:
                        self.mapa[y][x] = "🌾"

        # Gerar rios
        for i in range(5):  # Número de rios
            river_x = random.randint(0, self.largura - 1)
            river_y = random.randint(0, self.altura - 1)
            for _ in range(50):  # Tamanho do rio
                self.mapa[river_y][river_x] = "🌊"
                river_x += random.randint(-1, 1)
                river_y += random.randint(-1, 1)
                river_x = max(0, min(river_x, self.largura - 1))
                river_y = max(0, min(river_y, self.altura - 1))

    def imprimir_mapa(self):
        print(f"SEED utilizada: {self.seed}")
        print("MAPA:")
        for linha in self.mapa:
            print(" ".join(linha))

        print("\nTABELA DE LOCAIS:")
        for bioma, descricao in self.biomas.items():
            print(f"{bioma}: {descricao}")

# Exemplo de uso
def main():
    largura = 20
    altura = 20
    seed = input("Por favor, insira uma seed (ou pressione Enter para gerar aleatoriamente): ").strip()
    mapa = Mapa(largura, altura, seed)
    mapa.gerar_terreno()
    mapa.imprimir_mapa()

if __name__ == "__main__":
    main()