# Simple Bank System

from datetime import date

current_date = date.today()
brl_date = current_date.strftime('%d/%m/%Y')

balance = 0
extract = []
WITHDRAWAL_LIMIT_AMOUNT = 500
WITHDRAWAL_LIMIT_NUMBER = 3
withdraw_counter = 0

divisor = '-' * 45
divisor_output = '#' * 45


def menu():
  while True:
    print("Menu")
    print(divisor)
    print("1 - VIZUALIZAR SALDO\n2 - DEPÓSITO\n3 - SAQUE\n4 - EXTRATO\n0 - SAIR")
    print(divisor)
    option = input("Digite o número correspondente a opção que deseja: ")
    
    if option == "1":
      balance()

    elif option == "2":
      deposit(deposit_amount)
    
    elif option == "3":
      withdraw(withdraw_amount)
      
    elif option == "4":
      extract()
      
    elif option == "0":
      break
    
    else:
      print("!!!!! Operação inválida !!!!!!")
    
    
def balance():
  print(divisor_output)
  print(f"Seu saldo é de R${balance},00")
  print(divisor_output)
  
    
def deposit(deposit_amount, balance):
  deposit_amount = int(input("Digite o valor que deseja depositar: "))
  if deposit_amount > 1:
    balance += deposit_amount
    extract.append(f"Depósito - R${deposit_amount}")
    print(divisor_output)
    print(f"\nDepósito de R$:{deposit_amount},00 realizado com sucesso.\n")
    print(divisor_output)
  else:
    print(divisor_output)
    print("Valor inválido\n")
    print(divisor_output)
    
    
def withdraw(withdraw_amount):
  withdraw_amount = int(input("Digite o valor que deseja sacar: "))
  if withdraw_counter <= 3:
    if withdraw_amount <= WITHDRAWAL_LIMIT_AMOUNT and withdraw_amount <= balance:
      balance -= withdraw_amount
      extract.append(f"Saque - R${withdraw_amount}")
      withdraw_counter += 1
      print(divisor_output)
      print(f"\nSaque de R$:{withdraw_amount},00 realizado com sucesso. Novo saldo é de R$ {balance},00\n")
      print(divisor_output)
    else:
      print(divisor_output)
      print("\nSaque não poderá ser realizado.\n")
      print(divisor_output)
  else:
      print(divisor_output)
      print(f"\nVocê já realizou {WITHDRAWAL_LIMIT_NUMBER} saques, número máximo permitido por dia.\n")
      print(divisor_output)
    
    
  def extract():
    print("***************************************************")
    print(f"\nExtrato gerado em {brl_date} \n")
    print("***************************************************")
    print(extract)
  


print("\nBem Vindos ao Py Bank! Como podemos te ajudar?")
menu()

