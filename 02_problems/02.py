# Set pricing for movie ticket according to age group

age = int(input('Enter you age: '))
day = input('What is the day today: ')

price = 12 if age >= 18 else 8

if day.lower() == 'wednesday':
  price -= 2

print(f'${price}')

# def set_ticket_price(age, day):
#   price = None

#   if age >= 18:
#     price = 12
#   elif age <= 13:
#     price = 10

#   if day.lower() == 'wednesday':
#     price -= 2  

#   print(f'Ticket is ${price}')
#   return price

# set_ticket_price(age, day)
