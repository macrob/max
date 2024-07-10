import config
import requests

# my_file = open(config.PTH_PROJECT + '/main.py')
# print(my_file)

# print(my_file.read())
# print(my_file.close())
# print()


# with open(config.PTH_PROJECT + '/main.py') as my_file:
#     print(my_file.read())

# with open(config.PTH_PROJECT + '/new_file.txt', 'w') as my_file:
#     print(my_file.write('testtest'))


def get_filename(filename: str) -> str:
    return config.PTH_PROJECT + '/downloads/' + filename


def create_log(log: str, filename: str = 'log.txt'):
    with open(config.PTH_PROJECT + '/' + filename, 'a') as logfile:
        logfile.write(log + '\n')


def read_log(filename: str = 'log.txt'):
    with open(config.PTH_PROJECT + '/' + filename, 'r') as logfile:
        #   logs = logfile.read()
        # print(logs.split())

        # data = logfile.readlines()
        # print(data)

        line = logfile.readline()
        while line:
            print(line.strip())
            line = logfile.readline()


# create_log('testtest')
# create_log('testtest2')
# create_log('testtest3')

# read_log()


def download(filename: str, url: str):
    filename = get_filename(filename)
    with open(filename, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)


# url = 'https://t4.ftcdn.net/jpg/05/59/41/69/360_F_559416996_JgBW9B9DAyaBgyKJfxoOXSAUg44atD33.jpg'
# download('test.jpg', url)

def read(filename: str):
    filename = get_filename(filename)
    with open(filename, 'rb') as file:
        print(file.read())

def append_file(filename: str, text: str):
    filename = get_filename(filename)
    with open(filename, 'ab') as file:
        file.write(text)

file = 'test.jpg'
read(file)
append_file(file, b'123 Abaldet')
read(file)


print()
