# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Forca:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada = []
        self.letra_correta = []

    # Método para adivinhar a letra
    def chute(self, letra):
        if letra in self.palavra and letra not in self.letra_correta:
            self.letra_correta.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def forca_over(self):
        return self.forca_win() or (len(self.letra_errada) == 6)

    # Método para verificar se o jogador venceu
    def forca_win(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    # Método para não mostrar a letra no board
    def palavra_escondida(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letra_correta:
                rtn += '_'
            else:
                rtn += letra
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print((board[len(self.letra_errada)]))
        print('\nPalavra: ' + self.palavra_escondida())
        print('\nLetras erradas', )
        for letras in self.letra_errada:
            print(letras, )
        print()
        print('Letras corretas: ', )
        for letras in self.letra_correta:
            print(letras, )
        print()


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Forca(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.forca_over():
        game.print_game_status()
        user_input = input("\nDigite uma letra: ")
        game.chute(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.forca_win():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
