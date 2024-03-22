import random

# Função para escolher uma palavra aleatória da lista
def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php', 'cplusplus', 'swift', 'kotlin']
    return random.choice(words)

# Função para exibir a palavra com letras adivinhadas e espaços para letras não adivinhadas
def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Função principal do jogo
def hangman():
    print("Bem-vindo ao jogo da forca!")
    word = choose_word()  # Escolhe uma palavra aleatória
    guessed_letters = []  # Lista para armazenar as letras adivinhadas
    attempts = 6  # Número de tentativas disponíveis

    # Loop principal do jogo
    while True:
        print("\nPalavra:", display_word(word, guessed_letters))
        print("Tentativas restantes:", attempts)
        
        # Verifica se todas as letras foram adivinhadas
        if '_' not in display_word(word, guessed_letters):
            print("Parabéns! Você ganhou!")
            break

        # Verifica se o jogador usou todas as tentativas
        if attempts == 0:
            print("Você perdeu! A palavra era:", word)
            break
        
        guess = input("Digite uma letra ou a palavra inteira: ").lower()

        # Verifica se o palpite é válido (letra única ou palavra inteira)
        if len(guess) != 1 and guess != word or not guess.isalpha():
            print("Por favor, insira uma única letra válida ou a palavra inteira.")
            continue

        # Verifica se a letra ou a palavra já foi adivinhada
        if guess in guessed_letters:
            print("Você já tentou esta letra ou a palavra.")
            continue

        # Adiciona a letra ou a palavra à lista de letras adivinhadas
        guessed_letters.append(guess)

        # Verifica se o palpite é uma letra ou a palavra inteira e processa de acordo
        if len(guess) == 1:  # Se o palpite for uma letra
            if guess not in word:
                attempts -= 1  # Decrementa o número de tentativas se o palpite for incorreto
                print("Letra incorreta.")
            else:
                print("Letra correta!")
        else:  # Se o palpite for a palavra inteira
            if guess == word:
                print("Parabéns! Você ganhou!")
                break
            else:
                print("Palavra incorreta.")
                attempts -= 1  # Decrementa o número de tentativas se o palpite for incorreto

hangman()
