from typing import Callable

database = {
  'login': 'admin',
  'password': '<PASSWORD>'
}
def log_decorator(filename: str = 'log.csv') -> Callable:
  def _log_decorator(func: Callable):
    def wrapper(*args, **kwargs) -> dict:
      print(1111)
      result = func(*args, **kwargs)
      print(22222)
      with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{func.__name__}; {args}; {kwargs}; {result}\n')

      return result

    wrapper.__name__ = func.__name__
    return wrapper
  return _log_decorator


def auth_decorator(func: Callable):
  def wrapper(*args, **kwargs) -> dict:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    
    if database['login'] == login and database['password'] == password:
      print('Доступ разрешен')
    else:
      raise Exception('Доступ запрещен')

    print(3333)
    result = func(*args, **kwargs)
    print(4444)
    return result

  wrapper.__name__ = func.__name__
  return wrapper


def say_hello(name: str) -> None:
    print(f"Hello, {name}")
    
def say_hello_world() -> None:
    say_hello('World')
    
    
# say_hello('John')
# @auth_decorator
@log_decorator()
def add_two_numbers(a: int, b: int) -> int:
  result = a + b
  return result



@log_decorator()
def add_three_numbers(a: int, b: int, c: int) -> int:
  result = a + b + c
  return result

def wrapper(func: Callable, *args, **kwargs) -> dict:
  
  print(args)
  print(*args)
  print(kwargs)

  result = func(*args, **kwargs)
  return {'result': result}
  
# result = wrapper(add_two_numbers, 5, 2)
# print(result)

# result = wrapper(add_three_numbers, 5, 2, 4)

# print(result)

res = add_two_numbers(a=5, b=2)
print(res)
# result = wrapper(add_two_numbers, a=5, b=2)
# print(result)






res = add_three_numbers(5, 2.5, 4)
print(res)