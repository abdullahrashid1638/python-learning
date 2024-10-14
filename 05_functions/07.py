def sum_all(*args):
  print(*args)
  print(args)
  for i in args:
    print(i ** 2)
  return f'Sum is: {sum(args)}'

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6))

# Using loop

def sum_all_loop(nums = ()):
  sum = 0
  for n in nums:
    sum += n
  return f'Sum is: {sum}'

print(sum_all_loop((1, 2, 3))) 