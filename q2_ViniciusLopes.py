#Criar um usuário
users = lambda id, name, password: {'id': id, 'name': name, 'password': password}

#Criar uma transação
create_transaction = lambda user, value: {'user': user, 'value': value} if value > 0 else None

#Criar um depósito
cash = lambda transaction: {**transaction, 'type': 'cash'} if transaction and transaction['value'] > 0 else None
#Operação de depósito iniciada
receive_cash = lambda: print(f"*","-"*45,"*","\nThe deposit operation has been initiated.")
#Imprimir e retornar recibo de pagamento
print_and_return_payment_receipt = lambda received_cash_transaction: print(f"Payment receipt:\nUser ID: {received_cash_transaction['user']['id']}\nUser name: {received_cash_transaction['user']['name']}\nValue: ${received_cash_transaction['value']}.00") if received_cash_transaction else print('Invalid value for cash transaction.')

#Criar transferência de fundos
fund_transfer = lambda transaction, user: {**transaction, 'type': 'fund transfer', 'receiver': user} if transaction and transaction['value'] > 0 else None
#Operação de transferência iniciada
receive_fund_transfer = lambda: print(f"*","-"*45,"*","\nThe fund transfer operation has been initiated.")
#Fornecer detalhes de depósito bancário
print_and_return_bank_deposit_details = lambda transaction: (transaction and print(f"Bank deposit details:\nRemitter ID: {transaction['user']['id']}\nRemitter name: {transaction['user']['name']}\nValue: ${transaction['value']}.00\nReceiver ID: {transaction['receiver']['id']}\nReceiver name: {transaction['receiver']['name']}")) if isinstance(transaction, dict) else print('Invalid value for fund transfer transaction.')

#Credit
credit = lambda transaction: {**transaction, 'type': 'credit'} if transaction and transaction['value'] > 0 else None
#Operação de crédito iniciada
receive_credit = lambda user, transaction: print(f"*","-"*45,"*",f"\nThe credit operation has been initiated.\nUser ID: {user['id']}\nUser name: {user['name']}\nValue: ${transaction['value']}.00")
#Request payment from bank
request_payment_from_bank = lambda transaction: (print(f"* {'-' * 45} *\nPayment request sent to the bank.") or transaction) if transaction and transaction['value'] > 0 else None


#Confirmar pagamento pelo banco
confirm_payment_from_bank = lambda transaction: (print(f"* {'-' * 45} *\nThe payment has been confirmed by the bank.") or transaction) if transaction and transaction['value'] > 0 else None
#Cancelar transação
cancel_transaction = lambda transaction: (print('The operation was canceled.') and transaction.clear()) 
#Completar transação
complete_transaction = lambda transaction: (print('The operation failed, finishing... ') and transaction.clear()) if not transaction or transaction['value'] < 0 else (print('The operation was successful.\n') and transaction)



user1 = users(1, 'Vinicius', '123')
transaction1 = create_transaction(user1, 100)
cash1 = cash(transaction1)
receive_cash()
print_and_return_payment_receipt(cash1)
complete_transaction(cash1)
print(transaction1)

user2 = users(2, 'Lopes', '123')
transaction2 = create_transaction(user2, 100)
cash2 = cash(transaction2)
receive_cash()
print_and_return_payment_receipt(cash2)
complete_transaction(cash2)

user3 = users(3, 'Sosô', '123')
user4 = users(4, 'Vini', '123')
transaction3 = create_transaction(user3, 1000)
fund_transfer1 = fund_transfer(transaction3, user4)
receive_fund_transfer()
received_transaction = fund_transfer1
print_and_return_bank_deposit_details(received_transaction)
confirmed_transaction = confirm_payment_from_bank(received_transaction)
complete_transaction(confirmed_transaction)

user5 = users(5, 'John Doe', '1234')
credit_transaction = create_transaction(user5, 100)
credit(credit_transaction)
receive_credit(user5, credit_transaction)
request_payment_from_bank(credit_transaction)
confirm_payment_from_bank(credit_transaction)
complete_transaction(credit_transaction)

