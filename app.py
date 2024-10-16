import os

# lista - semelhante ao array do js
# restaurantes = ["Pizza", "Sushi"]

# dicionário -  semelhante ao objeto do js
restaurantes = [
  {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
  {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
  {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

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


def opcao_invalida():
  print('Opção inválida \n')
  input('Digite uma tecla para voltar ao menu principal \n')


def alternar_estado():
  print('Alternando estado do restaurante')
  nome_do_restaurante = input('Digite o nome do restaurante desejado para alternar o estado')
  restaurante_encontrado = False

  for restaurante in restaurante:
    if nome_do_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
      print(mensagem)
  if not restaurante_encontrado:
    print('O restaurante não foi encontrado')


  input('Digite uma tela para voltar ao menu principal')
  main()

# conceito de lista
def cadastrar_novo_restaurante():
  os.system('clear')
  print('Cadastro de novos restaurantes\n')
  nome_do_restaurante = input('Digite o nome do restaurante desejado para cadastrar: ')
  # método append semelhante ao push do JS
  categoria = input(f'Digite o nome da categoria do restaurante: ')
  dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
  restaurantes.append(dados_do_restaurante)

  print(f'O restaurante {dados_do_restaurante} foi cadastrado com sucesso \n')
  input('Digite uma tela para voltar ao menu principal')
  # volta para função principal
  main()


def listar_restaurante():
  os.system('clear')
  print('Listar restaurantes\n')

  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = restaurante['ativo']

    print(f"- {nome_restaurante} | {categoria} | {ativo}")
  
  input('Digite uma tela para voltar ao menu principal')
  main()

def escolher_opcao():
  try:
      opcao_escolhida = int(input('Escolha uma opção: '))
      # conceito de string literal
      # print(f'Você escolheu a opção {opcao_escolhida}')

      # aprendendo a usar o tipo de variável em python
      # print(type(opcao_escolhida))

      # condicionais
      if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
      elif opcao_escolhida == 2:
        listar_restaurante()
      elif opcao_escolhida == 3:
        alternar_estado()
      elif opcao_escolhida == 4:
        finalizar_app()
      else:
        opcao_invalida()
  except:
        opcao_invalida()


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
  os.system('clear')
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()


if __name__ == '__main__':
  main()