import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Tokenizer:
    def __init__(self, expressao):
        self.expressao = expressao
        self.posicao = 0

    def proximo_token(self):
        while self.posicao < len(self.expressao) and self.expressao[self.posicao].isspace():
            self.posicao += 1

        if self.posicao >= len(self.expressao):
            return Token('FIM', None)

        padrao_numero = r'\d+'
        padrao_operador = r'[+\-*/]'
        padrao_parenteses = r'[()]'

        if re.match(padrao_numero, self.expressao[self.posicao:]):
            match_numero = re.match(padrao_numero, self.expressao[self.posicao:])
            valor = int(match_numero.group())
            self.posicao += len(match_numero.group())
            return Token('NUMERO', valor)
        elif re.match(padrao_operador, self.expressao[self.posicao:]):
            valor = self.expressao[self.posicao]
            self.posicao += 1
            return Token('OPERADOR', valor)
        elif re.match(padrao_parenteses, self.expressao[self.posicao:]):
            valor = self.expressao[self.posicao]
            self.posicao += 1
            return Token('PARENTESES', valor)
        else:
            raise ValueError('Token inválido: ' + self.expressao[self.posicao])

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.token_atual = self.tokenizer.proximo_token()

    def expr(self):
        resultado = self.termo()

        while self.token_atual.tipo == 'OPERADOR' and self.token_atual.valor in ['+', '-']:
            operador = self.token_atual.valor
            self.avancar()
            if operador == '+':
                resultado += self.termo()
            elif operador == '-':
                resultado -= self.termo()

        return resultado

    def termo(self):
        resultado = self.fator()

        while self.token_atual.tipo == 'OPERADOR' and self.token_atual.valor in ['*', '/']:
            operador = self.token_atual.valor
            self.avancar()
            if operador == '*':
                resultado *= self.fator()
            elif operador == '/':
                resultado /= self.fator()

        return resultado

    def fator(self):
        if self.token_atual.tipo == 'NUMERO':
            resultado = self.token_atual.valor
            self.avancar()
            return resultado
        elif self.token_atual.tipo == 'PARENTESES' and self.token_atual.valor == '(':
            self.avancar()
            resultado = self.expr()
            if self.token_atual.tipo != 'PARENTESES' or self.token_atual.valor != ')':
                raise ValueError('Erro de sintaxe: Esperado ")"')
            self.avancar()
            return resultado
        else:
            raise ValueError('Erro de sintaxe: Esperado número ou "("')

    def avancar(self):
        self.token_atual = self.tokenizer.proximo_token()

def parse_expressao(expressao):
    tokenizer = Tokenizer(expressao)
    parser = Parser(tokenizer)
    return parser.expr()

# Exemplo de uso:
expressao = "3 + 4 * (5 - 2)"
resultado = parse_expressao(expressao)
print("Resultado:", resultado)  # Saída esperada: 15