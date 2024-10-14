# Calculate the sum of the even numbers upto a given number n

n = int(input('Enter the num: '))
even_sum = 0

for i in range(2, n + 1, 2):
    even_sum += i

print(f'Sum of even numbers upto {n} is {even_sum}')
