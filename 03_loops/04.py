# Reverse a string

string = input('Enter your string: ')
# string_len = len(string)
reversed_string = ''

# for i in range(string_len - 1, -1, -1):
#   reversed_string += string[i]

for char in string:
  reversed_string = char + reversed_string

print(f'Your reveresed string is {reversed_string}')
