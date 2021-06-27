blockchain = []
waiting_for_input = True

def get_last_blockchain_value():
  return None if len(blockchain) < 1 else blockchain[-1]

def add_value(transaction_amount, last_tx):
  safe_last_tx = [1] if last_tx == None else last_tx
  blockchain.append([safe_last_tx, transaction_amount])

def print_blockchain():
  for index in range(0, len(blockchain)):
      print('Block number ' + str(index) + ':')
      print(blockchain[index])

def verify_chain(index=0):
  if len(blockchain) in [0, 1] or index == len(blockchain) - 1:
    return True
  elif blockchain[index] != blockchain[index + 1][0]:
    return False
  else:
    verify_chain(index+1)

while waiting_for_input:
  print('Please choose')
  print('1: Add a new transaction value')
  print('2: Output blockchain values')
  print('h: Manipulate the chain')
  print('q: Close script: ')
  
  option = input('Your choice: ')

  if option == '1':
    value = float(input('Your transaction amount please: '))
    add_value(value, get_last_blockchain_value())
  elif option == '2':
    print_blockchain()
  elif option == 'h':
    if len(blockchain) > 0:
      blockchain[0] = [2]
  elif option == 'q':
    waiting_for_input = False
  else:
    print('This option is not allowed, please pick a value from the list')
  
  if verify_chain() == False:
    print('Blockchain is invalid')
    break
  else:
    print('-'*20)
print('Bye!')
exit()