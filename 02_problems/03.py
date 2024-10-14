# Grade calculator

def calculate_grades():
  percentage = int(input('Enter your percentage: '))

  if percentage > 100:
    print('Percentage is wrong')
    return

  grade = None

  if percentage >= 90:
    grade = 'A+'
  elif percentage >= 80:
    grade = 'A'
  elif percentage >= 70:
    grade = 'B'
  elif percentage >= 60:
    grade = 'C'
  else:
    grade = 'F'

  print(f'Your grade is \'{grade}\'')
  return grade

calculate_grades()
