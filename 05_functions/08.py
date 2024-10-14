def print_kwargs(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f'{key}: {value}')

print_kwargs(name = 'Alice', power = 'Disguise')
print_kwargs(name = 'Alice')
print_kwargs(name = 'Alice', power = 'Disguise', enemy = 'Woodland Witch')
  