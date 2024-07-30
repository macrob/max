"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - 
1.1 програмно добавити одного студента, 
1.1.1 Зробити функцію яка виведе в браузер форму та повертає дані студента:
1.1.1.1 Які данні і скільки полів повина мати форма, дивимось на дані в БД (students)

1.1.2 зробити функцію яка буде добавляти студента, аргумент функціі данні студента з форми, функція нічого не повертає, але добавляє в БД
1.1.2.1 зробити функцію яка буде робити конвертацію/переклад англіских назв ключей на україньску. Тобто аргумент функції англіське слово, 
повертає фунція україньске слово.

якщо подивись на формат данних у бд та данні які повернулись з форми, то вони мають разні ключи, в бд в нас
ключами є 
Пошта
Вік
Номер телефону
Середній бал
з форми input_student поверає данні с ключами на англіскій мові. 

1.1.2.2 зробити функцію яка повертає ключ для БД (students - наша БД), наприклад 
input_student = {
    first_name: 'Сергій'
    last_name: 'Єпішкін'
    age: 37
    .... інші поля
}
Ключем до БД є 'Сергій Єпішкін'


2 -
2.1 створити список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
2.1.1 функція яка повертає список гарних студентів, аргументи функціі, дикшенарі studentds, там середній бал по якому ми робимо фільтрацію
функція повертає список в форматі [ФІО, середній бал]

2.2 вивести на екран, формат наповнення цього списку up to you
2.2.1 створити функцію яка виводить на єкран список гарніх студентів. аргумент функціі
список в форматі good_students = [
    ['Сергій Єпішкін', 80],
    ['Максим Єпішкін', 90],
]. Виводим інво таблицєю 

3
3.1 - визначити середній бал по групі
3.1.1 функція аргумент якої studentds БД, функція повертає середній бал
3.2 - вивести на екран
3.2.1 функція виводу на єкран середнього балу, аргумент функції серелній бал, нічого не повертає

4 вывести на экран список студентів, при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)
4.1 зробити список
4.1.1 функція яка повертає список студентів, аргумент функціі students (наша БД), функця повертає
список [
    [
        name,
        avg_mark,
        phone, - якщо телефон не вказаний ставимо якись дефолтний, чи повідомлення що номер не вказано
        email - якщо імейл не вказаний ставимо якись дефолтний, чи повідомлення що імейл не вказано
    ]
]
4.2 вывести на экран список студентів
4.2.1
зробити функцію яка виводить через таблицю список стундентів. аргумент функції 
cписок яки повернулся функція 4.1.1

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8,
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5,
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80,
    },
}

# ваш код нижче !!!!!!!! вище нічого не змінюємо


from pywebio import start_server
from pywebio.output import put_text, put_table, put_html
from pywebio.input import (
    input as input_pw,
    input_group,
    slider,
)

import config
import constants
from utils import reload_page

def translate_field(key):
    return constants.FORM_KEYS_TRANSLATE[key]

EMAIL = translate_field('email')
AGE = translate_field('age')
PHONE = translate_field('phone')
AVG_MARK = translate_field('avg_mark')



def get_dict_key(input_student: dict) -> str:
    fname = input_student.get('fname')
    lname = input_student.get('lname')
    return fname +'' + lname
    
def add_student(input_student):
    student = {
        EMAIL: input_student.get('email'),
        AGE: input_student.get('age'),
        PHONE: input_student.get('phone'),
        AVG_MARK: input_student.get('avg_mark'),
    }
    
    key = get_dict_key(input_student)
    students[key] = student
    pass


def request_student_data():
    student = input_group(
        constants.MSG_FORM_TITLE,
        [
            input_pw(constants.MSG_REQUEST_FIRST_NAME, name='fname', required=True),
            input_pw(constants.MSG_REQUEST_LAST_NAME, name='lname', required=True),
            input_pw(constants.MSG_REQUEST_EMAIL, name='email', required=True),
            slider(constants.MSG_REQUEST_AGE, name='age', min_value=18, max_value=40),
            input_pw(constants.MSG_REQUEST_PHONE, name='phone', required=False),
            slider(
                constants.MSG_REQUEST_MARK,
                name='avg_mark',
                min_value=0.0,
                max_value=100.0,
            ),
        ],
    )
    return student


def get_good_students(students: dict, avg_mark: int) -> list:
    result = []
    for name, studentData in students.items():
        student_avg_mark = studentData[AVG_MARK];
        if student_avg_mark >= avg_mark:
            result.append([name, student_avg_mark])
    return result


def show_good_students(good_students: list):
    put_html(constants.MSG_GOOD_STUDENTS)
    put_table(
        good_students, [constants.LABEL_TABLE_NAME, constants.LABEL_TABLE_AVG_MARK]
    )


def get_avg_group_mark(students: dict) -> float:
    result = 0
    for student in students.values():
        student_avg_mark = student[AVG_MARK]
        result += student_avg_mark
    return result / len(students)


def show_avg_group_mark(avg_group_mark: float):
    put_html(constants.MSG_GROUP_AVG_MARK.format(avg_group_mark=round(avg_group_mark, 2)))


def get_students(students: dict) -> list:
    result = []
    for name, studentData in students.items():
        result.append([
            name, 
            studentData.get(AVG_MARK),
            studentData.get(PHONE) or constants.MSG_PHONE_NOT_FOUND,
            studentData.get(EMAIL) or constants.MSG_EMAIL_NOT_FOUND,
        ])

    return result
    
def show_students(students: list) -> None:
    put_html(constants.MSG_STUDENTS_LIST)
    put_table(students, [
        constants.LABEL_TABLE_NAME,
        constants.LABEL_TABLE_AVG_MARK,
        constants.LABEL_TABLE_PHONE,
        constants.LABEL_TABLE_EMAIL
    ])
    

def main():
    student = request_student_data()
    add_student(student)

    good_students = get_good_students(students, 50)
    show_good_students(good_students)

    avg_group_mark = get_avg_group_mark(students)
    show_avg_group_mark(avg_group_mark)

    students_list = get_students(students)
    show_students(students_list)

    reload_page(config.PAGE_RELOAD_INTERVAL_MS)

if __name__ == '__main__':
    start_server(main, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)


def get_avg_mark_group(students: dict) -> float:
    result = 0

    students_list = students.values()
    students_count = len(students_list)

    for student_data in students_list:
        student_avg_mark = student_data.get(translate_key('avg_mark'))
        result += student_avg_mark

    result /= students_count

    return result