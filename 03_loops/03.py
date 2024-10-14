# Print the multiplication table for a given number upto 10

n = int(input('Enter the number: '))

for i in range(1, 10 + 1):
  if i == 5:
    continue
  print(f'{n} X {i} = {n * i}')
