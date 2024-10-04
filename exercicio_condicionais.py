# 1
# numero = int(input('Digite um número: '))

# def par_ou_impar(numero):
#   if numero % 2 == 0:
#     print(f'O número {numero} é par \n')
#   else:
#     print(f'O número {numero} é impar \n')


# par_ou_impar(numero)

# 2
# idade = int(input('Digite sua idade: '))

# def classificacao(idade):
#   if idade <= 12:
#     print('Criança')
#   elif 13 <= idade <= 18:
#     print('Adolescente')
#   else:
#     print('Adulto')

# classificacao(idade)

# 3
login = input('Digite seu login: ')
password = input('Digite sua senha: ')

def check_login(login, password):
  if login == '' or password == '':
    print('O login ou senha não podem estar vazios')
  elif login != 'adm' and password != '123':
    print('Login ou Senha errados')
  else:
    print('Logado(a) no sistema')

check_login(login, password)