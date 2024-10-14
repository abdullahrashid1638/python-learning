channel = 'chai aur code'

def scope():
  channel = 'bro code'
  print(channel)

scope()

print(channel)

x = 99

# def func2(y):
#   z = x + y
#   return z

# print(func2(2))

# def func3():
#   global x
#   x = 12

# func3()

# print(x)

def f1():
  x = 88
  def f2():
    print(x)
  return f2

result = f1()

result()

print(x)

def chaicoder(n):
  def actual(x):
    return x ** n
  return actual

sqr = chaicoder(2)
cube = chaicoder(3)

print(sqr(2))
print(sqr(3))
