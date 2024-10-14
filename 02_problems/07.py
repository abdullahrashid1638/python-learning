# Calculate leap year

year = int(input('Enter the year: '))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       is_leap_year = True
#     else:
#       is_leap_year = False
#   else:
#     is_leap_year = True

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  is_leap_year = True
else:
  is_leap_year = False

if is_leap_year:
  print(f'{year} is a leap year')
else:
  print(f'{year} is not a leap year')

