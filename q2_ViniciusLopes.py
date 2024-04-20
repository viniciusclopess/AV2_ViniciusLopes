#Criar um usuário
users = lambda id, name, password: {'id': id, 'name': name, 'password': password}

#Criar uma transação
create_transaction = lambda user, value: {'user': user, 'value': value} if value > 0 else None

#Criar um depósito
cash = lambda transaction: {**transaction, 'type': 'cash'} if transaction and transaction['value'] > 0 else None
#Operação de depósito iniciada
receive_cash = lambda: print(f"\n*","-"*45,"*","\nThe deposit operation has been initiated.")
#Imprimir e retornar recibo de pagamento
print_and_return_payment_receipt = lambda received_cash_transaction: print(f"Payment receipt:\nUser ID: {received_cash_transaction['user']['id']}\nUser name: {received_cash_transaction['user']['name']}\nValue: ${received_cash_transaction['value']}.00") if received_cash_transaction else print('Invalid value for cash transaction.')

#Criar transferência de fundos
fund_transfer = lambda transaction, user: {**transaction, 'type': 'fund transfer', 'receiver': user} if transaction and transaction['value'] > 0 else None
#Operação de transferência iniciada
receive_fund_transfer = lambda: print(f"\n*","-"*45,"*","\nThe fund transfer operation has been initiated.")
#Fornecer detalhes de depósito bancário
print_and_return_bank_deposit_details = lambda transaction: (transaction and print(f"Bank deposit details:\nRemitter ID: {transaction['user']['id']}\nRemitter name: {transaction['user']['name']}\nValue: ${transaction['value']}.00\nReceiver ID: {transaction['receiver']['id']}\nReceiver name: {transaction['receiver']['name']}")) if isinstance(transaction, dict) else print('Invalid value for fund transfer transaction.')

#Credito
credit = lambda transaction: {**transaction, 'type': 'credit'} if transaction and transaction['value'] > 0 else None
#Operação de crédito iniciada
receive_credit = lambda user, transaction: print(f"\n*","-"*45,"*",f"\nThe credit operation has been initiated.\nUser ID: {user['id']}\nUser name: {user['name']}\nValue: ${transaction['value']}.00")
#Request payment from bank
request_payment_from_bank = lambda transaction: (print(f"* {'-' * 45} *\nPayment request sent to the bank.") or transaction) if transaction and transaction['value'] > 0 else None


#Confirmar pagamento pelo banco
confirm_payment_from_bank = lambda transaction: (print(f"||{'|' * 45}||\nThe payment has been confirmed by the bank.") or transaction) if transaction and transaction['value'] > 0 else None
#Cancelar transação
cancel_transaction = lambda transaction: (print('The operation was canceled.') and transaction.clear())
#Completar transação
complete_transaction = lambda transaction: (print('The operation failed, finishing... ') and transaction.clear()) if not transaction or transaction['value'] < 0 else (print('The operation was successful.') and transaction)

#teste 1
user = users('1', 'Vinicius Lopes', '123')
transaction = create_transaction(user, 100)
receive_cash()
transaction = cash(transaction)
print_and_return_payment_receipt(transaction)
confirm_payment_from_bank(transaction)
complete_transaction(transaction)

#teste 2
user = users('2', 'Sophia Brito', '456')
user2 = users('3', 'Unifor', '789')
transaction = create_transaction(user, 200)
receive_fund_transfer()
transaction = fund_transfer(transaction, user)
print_and_return_bank_deposit_details(transaction)
confirm_payment_from_bank(transaction)
complete_transaction(transaction)

#teste 3
user = users('3', 'Maria Silva', '789')
transaction = create_transaction(user, 300)
receive_credit(user, transaction)
transaction = credit(transaction)
request_payment_from_bank(transaction)
confirm_payment_from_bank(transaction)
complete_transaction(transaction)

#Teste de Stress
import random, time

# Função de teste de estresse
stress_test = lambda num_transactions: [
    cash(create_transaction(users(1, 'John', 'password'), random.randint(1, 100)))

    for _ in range(num_transactions)
]
# Registrar o tempo inicial
start_time = time.time()

# Executar o teste de estresse com 100000 transações
transactions = stress_test(100000)

# Registrar o tempo final
end_time = time.time()

# Calcular o tempo total do teste
elapsed_time = end_time - start_time

# Exibir o tempo total do teste
print(f"Teste de estresse concluído em {elapsed_time:.2f} segundos.")

