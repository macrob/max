from pywebio import start_server
import requests
from pprint import pprint

import tkinter as tk
from pywebio.output import put_text, put_table, put_html
import config, constants, utils
import console

API_URL_ASTRONAUTS = 'http://api.open-notify.org/astros.json'
API_URL_USERS = 'https://dummyjson.com/users'

#RENDER_TYPE: 'console' | 'pywebio' | 'tkinter' = 'console'
RENDER_TYPE: str = 'console'
def get_astronauts() -> list[dict]:
  astronauts_response = requests.get(API_URL_ASTRONAUTS).json()
  astronauts_list = astronauts_response['people']
  return  astronauts_list

def get_astronauts_names() -> list[str]:
  astronauts_list: list[dict] = get_astronauts()
  
  result = []
  for astronauts in astronauts_list:
    result.append(astronauts['name'])
  return result


def get_users(limit: int=25, skip: int = 0) -> list[dict]:
  params = {
    'limit': limit,
    'skip': skip
  }

  users_response = requests.get(API_URL_USERS, params).json()
  return users_response.get('users')

def filter_users_by_age(users_list: list[dict], age: int) -> list[dict]:
  result = []
  for user in users_list:
    if user['age'] == age:
      result.append(user)

  return result

def get_users_names(users_list: list[dict]) -> list[str]:
  result = []
  for user in users_list:
    result.append(f'{user['firstName']} {user['lastName']}')
  return result

def get_users_names_by_age(age: int) -> list[str]:
  start = 0;
  limit = 50;

  users_names = []
  
  
  while True:
    chunk_users = get_users(skip=start, limit=limit)
    if not chunk_users:
      break

    start += limit

    filtered_users = filter_users_by_age(chunk_users, age)
    users_names += get_users_names(filtered_users)
    
  return users_names

def get_union_table(astros: list[str], users: list[str]) -> list[list[str]]:
  count = max([len(astros), len(users)])
   
  result = []  
  for iterator in range(count):
      astro: str = astros.pop() if astros else ''
      user: str = users.pop() if users else ''
      result.append([astro, user])

  return result

def show_table_by_pywebio(astros: list[str], users: list[str]) -> None:
  table = get_union_table(astros, users)

  put_table([['Astros', 'Users']] + table)

def show_table_in_console(astros: list[str], users: list[str]) -> None:
  max_length_astro = len(max(astros, key=len))
  max_length_user = len(max(users, key=len))

  table = get_union_table(astros, users)
  
  header_column_1 = 'Astros'
  header_column_2 = 'Users'

  header_length_1 = max(len(header_column_1), max_length_astro) + 2
  header_length_2 = max(len(header_column_2), max_length_user) + 2
  
  HR = f'+{console.hr(header_length_1 + 2)}+{console.hr(header_length_2 + 2)}+'
  print(HR)

  print(f'| {console.print_text(header_column_1, header_length_1)} | {console.print_text(header_column_2, header_length_2)} |')
  print(HR)
    
  for astro, user in table:
    print(
     ''.join([
        '| ',
        console.print_text(astro, header_length_1),
        ' | ',
        console.print_text(user, header_length_2),
        ' |'
      ])
    )

  # Print footer
  print(HR)
  
def show_table_by_console(astros: list[str], users: list[str]) -> None:  
  table = get_union_table(astros, users)
  console.put_table(table, ['Astros', 'Users'])
   

def show_table_by_tkinter(astros: list[str], users: list[str]) -> None:
  root = tk.Tk()
  root.title('Homework 11')

  # Create headers
  tk.Label(root, text='Astros', borderwidth=1, relief='solid', width=15).grid(row=0, column=0)
  tk.Label(root, text='Users', borderwidth=1, relief='solid', width=15).grid(row=0, column=1)

  table = get_union_table(astros, users)

  for iterator, (astro, user) in enumerate(table, start=1):
    tk.Label(root, text=astro, borderwidth=1, relief='solid', width=15).grid(row=iterator, column=0)
    tk.Label(root, text=user, borderwidth=1, relief='solid', width=15).grid(row=iterator, column=1)

  root.mainloop()

def main():
  users_age = 28
  # astros = get_astronauts_names()
  # users = get_users_names_by_age(users_age)

  astros = [
    'Luke Skywalker',
    'C-3PO',
    'R2-D2',
    'Darth Vader',
    'Leia Organa',
    'Owen Lars',
    'Beru Whitesun lars',
    'R5-D4',
    'Biggs Darklighter',
    'Obi-Wan Kenobi',
  ];

  users = [
    'Luke Skywalker',
    'Sebastian Vega',
    'Han Solo',
    'Wilhuff Tarkin',
    'Jar Jar Binks',
  ]
  
  # show_table_by_console(astros, users)
  switch = {
    'pywebio': show_table_by_pywebio,
    'console': show_table_by_console,
    'tkinter': show_table_by_tkinter,
  }
  switch[RENDER_TYPE](astros, users)
  
if __name__ == '__main__':
  if RENDER_TYPE == 'pywebio':
    start_server(main, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
  else:
    main()


