# Age Group Categorization

age = int(input('Enter you age: '))

def classify_age_group(age):
  if age < 13:
    print('Child')
  elif age >= 13 and age <= 19:
    print('Teenager')
  elif age >= 20 and age <= 59:
    print('Adult')
  else:
    print('Senior 60+')

classify_age_group(age)
