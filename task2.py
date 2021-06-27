name_list = ['pepe', 'maria', 'juan']

for name in name_list:
  name_len = len(name)
  if name_len > 5:
    print(str(name) + ' with length ' + str(len(name)))
  elif name.__contains__('n') or name.__contains__('N') > 0:
    print(str(name) + ' contains n or N')
  
while len(name_list) > 0:
  print(name_list)
  name_list.pop()
print(name_list)

