# Find number of positive numbers in an array

nums = [1, -2, 3, 4, -5, -6, 7, -8, 9]
positive_nums = 0

for n in nums:
  if n > 0:
    positive_nums += 1

print(f'Positive numbers are {positive_nums}')
