import os

def exibir_nome_programa():
  print('Sabor Express \n')

def finalizar_app():
  # recurso para limpar console
  os.system('clear')
  print('Encerrando o programa\n')


def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurantes')
  print('3. Ativer restaurante')
  print('4. Sair \n')

def escolher_opcao():
  opcao_escolhida = int(input('Escolha uma opção: '))
  # conceito de string literal
  # print(f'Você escolheu a opção {opcao_escolhida}')

  # aprendendo a usar o tipo de variável em python
  # print(type(opcao_escolhida))

  # condicionais
  if opcao_escolhida == 1:
    print('Cadastrar restaurante')
  elif opcao_escolhida == 2:
    print('Listar restaurantes')
  elif opcao_escolhida == 3:
    print('Ativer restaurante')
  else:
    finalizar_app()

  # abordagem usando match substitui o if/elseif
  # opcao_escolhida = int(input('Escolha uma opção: '))
  # match opcao_escolhida:
  #   case 1:
  #       print('Adicionar restaurante')
  #   case 2:
  #       print('Listar restaurantes')
  #   case 3:
  #       print('Ativar restaurante')
  #   case 4:
  #       print('Finalizar app')
  #   case _:
  #       print('Opção inválida!')


# definindo o main do python
# util para configurar ordem da chamada de funções

def main():
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()


if __name__ == '__main__':
  main()