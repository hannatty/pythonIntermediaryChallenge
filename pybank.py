from datetime import date
import textwrap

current_date = date.today()
brl_date = current_date.strftime('%d/%m/%Y')

balance = 0
extract_mov = ""
WITHDRAWAL_LIMIT_AMOUNT = 500
WITHDRAWAL_LIMIT_NUMBER = 3
withdraw_counter = 0

users = []
accounts = []

divisor = '-' * 45
divisor_output = '#' * 45

def menu():
  menu = """ \n
  ******************* MENU *******************
  [1]\tVer Saldo
  [2]\tDepositar
  [3]\tSacar
  [4]\tExtrato
  [5]\tCadastrar Usuário
  [6]\tCriar Nova Conta
  [7]\tListar Contas
  [0]\t SAIR
  """
  return input(textwrap.dedent(menu))
            
######### Bank Methods #########

def see_balance():
    print(divisor_output)
    print("")
    print(f"Seu saldo é de R${balance},00")
    print("")
    print(divisor_output)

def deposit(balance, deposit_amount, extract_mov, / ):
  if deposit_amount > 0:
    balance += deposit_amount
    extract_mov += f"Depósito - R${deposit_amount}"
    print(divisor_output)
    print("")
    print(f"\nDepósito de R$:{deposit_amount},00 realizado com sucesso.\n")
    print("")
    print(divisor_output)
  else:
      print(divisor_output)
      print("")
      print("Valor inválido\n")
      print("")
      print(divisor_output)
      
  return balance, extract_mov

def withdraw(*, balance, withdraw_amount, extract, WITHDRAWAL_LIMIT_AMOUNT, WITHDRAWAL_LIMIT_NUMBER, withdraw_counter):
    balance_exceeded = withdraw_amount > balance
    limit_exceeded = withdraw_amount > WITHDRAWAL_LIMIT_AMOUNT
    withdraw_number_exceeded = withdraw_counter >= WITHDRAWAL_LIMIT_NUMBER
    
    if balance_exceeded:
      print("Saldo insuficiente.")
    
    elif limit_exceeded:
      print("Valor informado excede limite permitido para saques.")
    
    elif withdraw_number_exceeded:
      print("Limite de saques diários excedido.")
      
    elif withdraw_amount > 0:
      balance -= withdraw_amount
      extract_mov += f"Depósito - R${withdraw_amount}"
      withdraw_counter += 1
      print(divisor_output)
      print("")
      print(f"\nSaque de R$:{withdraw_amount},00 realizado com sucesso. Novo saldo é de R$ {balance},00\n")
      print("")
      print(divisor_output)
    else:
      print(divisor_output)
      print("")
      print("\nValor informado é inválido.\n")
      print("")
      print(divisor_output)
      
    return balance, extract_mov

def show_extract(balance, /, *, extract):
  if extract_mov.isEmpty():
    print("***************************************************")
    print("Até o momento, não foram realizadas movimentações.")
    print("***************************************************")
  else:
    print("")
    print(f"\nExtrato gerado em {brl_date} \n")
    print(extract_mov)
    print(f"\nSeu saldo atual é de R$ {balance}")
    print("***************************************************")
    print("")
    
######### User Methods #########
def check_cpf(cpf):
  if cpf.len() < 11:
    print("CPF inválido. Número de dígitos inferior a 11.")
  elif cpf in users:
    print(f"O CPF informado, já existe em nosso cadastro.")
  else:
    users.append(cpf)
    print("CPF cadastrado com sucesso.")
    
def check_user_name(user_name):
  if user_name.len() < 5:
    print("Nome precisa conter mínimo de 5 caracteres")
  else:
    print("Nome cadastrado com sucesso.")
    
def check_address():
  print("Heelo")
  
def create_user(users):
  print("Iniciando cadastramento de novo usuário...")
  cpf = input("Digite seu cpf, APENAS NÚMEROS: ")
  user = filter_user(cpf, users)
  
  if user:
    print("O cpf informado já está associado a um usuário constante em nossa base de dados.")
    return
  
  user_name = input("Digite seu nome completo: ")
  birth_date = input("Digite sua data de nascimento (dd-mm-aaaa): ")
  address= input("Digite seu endereço (logradouro, número - bairro - cidade/sigla do estado): ")
  
  users.append({"user_name": user_name, "birth_date": birth_date, "cpf": cpf, "address": address})
  print("\nCadastro de usuário realizado com sucesso!\n")

def filter_user(cpf, users):
  filtered_users = [user for user in users if user["cpf"] == cpf]
  return filtered_users[0] if filtered_users else None
        
def create_account(AGENCY, account_number, users):
  cpf = input("Digite o cpf do usuário (APENAS NÚMEROS): ")
  user = filter_user(cpf, users)
  
  if user:
    print("Criação da conta realizada com sucesso!")
    return {"agency": AGENCY, "account_number": account_number, "user": user}
  else:
    print("Usuário não foi localizado no sistema. Conta não poderá ser criada. Cadastre primeiro o usuário.")
        
def list_accounts(accounts):
  for account in accounts:
    line = f"""\
      Agência:\t{account['agency']}
      C/C:\t{account['account_number']}
      Usuário:\t{account['user']['user_name']}
    """
    print(divisor_output)
    print(textwrap.dedent(line))
  
def main():
  WITHDRAWAL_LIMIT_NUMBER = 3
  AGENCY = "0001"
  WITHDRAWAL_LIMIT_AMOUNT = 500
  
  current_date = date.today()
  brl_date = current_date.strftime('%d/%m/%Y')
  balance = 0
  withdraw_counter = 0
  extract_mov = ""
  users = []
  accounts = []

  divisor = '-' * 45
  divisor_output = '#' * 45
  
  while True:
    option = menu()
      
    if option == "1":
      see_balance()
      
    elif option == "2":
      deposit_amount = float(input("Digite o valor que deseja depositar: "))
      balance, extract_mov = deposit(balance, deposit_amount, extract_mov)

    elif option == "3":
      withdraw_amount = float(input("Digite o valor que deseja sacar: "))
      balance, extract_mov = withdraw(
        balance=balance,
        withdraw_amount=withdraw_amount,
        extract_mov=extract_mov,
        withdraw_limit_amount=WITHDRAWAL_LIMIT_AMOUNT,
        withdraw_limit_number=WITHDRAWAL_LIMIT_NUMBER,
        withdraw_counter=withdraw_counter,
      )

    elif option == "4":
      show_extract(balance, extract_mov=extract_mov)
    
    elif option == "5":
      create_user(users)
            
    elif option == "6":
      account_number = len(accounts) + 1
      account = create_account(AGENCY, account_number, users)
      
      if account:
        accounts.append(account)
        
    elif option == "7":
      list_accounts(accounts)
    
    elif option == "0":
      break

    else:
      print("!!!!! Operação inválida !!!!!!")    
    
main()
