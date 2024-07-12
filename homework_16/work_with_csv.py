import config
import csv

def read_data_1(filename: str) -> list:
  with open(config.PTH_PROJECT + filename, mode='r', encoding='utf8') as file:
    data = file.read()
    data = data.split('\n')
    
    for row in data:
      row_info = row.split(',')
      row_age = row_info[3].strip()

      is_age = row_age.isdigit()
      
      if is_age:
        age_numeric = int(row_age)
        print(age_numeric * 88)
  

def read_data_2(filename: str) -> list:
  with open(config.PTH_PROJECT + filename, mode='r', encoding='utf8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
      print(row)

def main():
  read_data_2('/data.csv', delimiter=',')

if __name__ == '__main__':
  main()