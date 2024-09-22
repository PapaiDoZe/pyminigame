from models.calcular import Calcular
# Importamos do nosso módulo "calcular" a nossa classe "Calcular" para iniciar a execução do game.


def main() -> None:
    """Criamos a função main() que irá realizar o início do game e setar a pontuação em 0."""
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    """Esta função basicamente utiliza a classe 'Calcular', seus métodos e propertys para gerar a execução
    do jogo."""
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar jogando [1 - sim, 0 - não]? '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print(f'Até a próxima!')


if __name__ == '__main__':
    main()
# Utilizamos esse if para garantir que o jogo só será iniciado se o usuário estiver utilizando este arquivo
# principal
