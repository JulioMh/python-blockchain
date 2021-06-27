name = 'Julio'
age = 23

def print_args(firstArg, secondArg):
  print(str(firstArg) + ' ' + str(secondArg))

def decadesAlive(name, age):
  print(str(name) + ' has lived ' + str(int(age/10)) + ' decades' )

print_args(name, age)
decadesAlive(name, age)