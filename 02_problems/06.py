# Check password strength

password = input('Password: ')
password_len = len(password)

if password_len < 6:
  print('Your password is weak')
elif password_len >= 6 and password_len <= 10:
  print('Your password is medium')
else:
  print('Your password is strong')
