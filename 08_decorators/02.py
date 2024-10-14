def debug(func):
    def wrapper(*args, **kwargs):
        arguments = ', '.join(str(arg) for arg in args)
        keyword_arguments = ', '.join(f'{key} = {value}' for key, value in kwargs.items())
        print(f'Calling: {func.__name__} with arguments {arguments if arguments else 0} and keyword arguments {keyword_arguments if keyword_arguments else 0}')
        return func(*args, **kwargs)    
    return wrapper

@debug
def hello():
    print('hello')

hello()

@debug
def greet(name, greeting = 'Hello'):
    print(f'{greeting}, {name}')

greet('chai', greeting = 'hanji')
