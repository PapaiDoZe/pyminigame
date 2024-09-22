from random import randint
# Fazemos o import da biblioteca random e da função randint que serão cruciais na construção do game.

class Calcular:
    """Criando a classe calcular que irá fazer todos as operações matemáticas e gerar os números
    que iremos utilizar para fazer o usuário jogar."""
    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    """Acima temos algumas propertys criadas com fim de retornar os valores necessários nas funções seguintes,
    uma vez que os atributos da classe Calcular são privados."""

    def __str__(self: object) -> str:
        """Esta função serve para escrever na tela as informações da rodada que o jogador estará utilizando.
        Também atribui o nome da operação que estará sendo realizada."""
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        """A função identifica o valor gerado no atributo dificuldade da classe Calcular e gera dois valores
        para valor1 e valor2 com base na dificuldade."""
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:
        """Identifica os valores de valor1 e valor2, assim como a operação que foi selecionada aleatóriamente
        e resolve a operação matemática, definindo assim o resultado correto."""
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        """Com base no atributo 'operação', essa property retorna o símbolo relativo à operação que está
        sendo realizada."""
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        """Esta função recebe o valor gerado para 'resultado' e checa se o valor digitado pelo jogador está
        condizendo com o valor corredo."""
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        """Apenas exibe os valores e a operação que está sendo realizada."""
        print(f'{self.valor1} {self._op_simbolo} {self.valor2}')


