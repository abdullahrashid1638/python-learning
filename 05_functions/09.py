# # Tradidional way

# def even_numbers(limit):
#   even_nums = []
#   for n in range(2, limit + 1, 2):
#     even_nums.append(n)
#   return even_nums

# print(even_numbers(10))

def even_generator(limit):
  for n in range(2, limit + 1, 2):
    yield n
  
for n in even_generator(10):
  print(n)
