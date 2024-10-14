# from hello_chai import chai

# chai('tea')

chai = 'Masala Chai'

def formart_string(str, end):
  for index, letter in enumerate(str):
    if index == len(str) - 1:
      print(letter)
    elif str[index + 1] == ' ' or letter == ' ':
      print(letter, end='')
    else: 
      print(letter, end=end)

# formart_string(chai, '_')

keys = ['Masala', 'Ginger', 'Lemon']
values = ['Spicey', 'Zesty', 'Citrus']

# def create_dict(keys, values):
#   d = dict.fromkeys(keys, '')
#   for i, (key, value) in enumerate(d.items()):
#     d[key] = values[i]

#   return d

def create_dict(keys, values):
    return dict(zip(keys, values))

print(create_dict(keys, values))
