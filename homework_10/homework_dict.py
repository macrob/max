"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

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


def get_form_key(key):
    return constants.FORM_KEYS[key]


def add_student(input_student):
    fname = input_student.pop('fname')
    lname = student.pop('lname')
    key = fname + ' ' + lname
    
    student = {
        get_form_key('email'): input_student.pop('email'),
        get_form_key('age'): input_student.pop('age'),
        get_form_key('phone'): input_student.pop('phone'),
        get_form_key('avg_mark'): input_student.pop('avg_mark'),
    }
    
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
        if studentData[get_form_key('avg_mark')] >= avg_mark:
            result.append([name, studentData[get_form_key('avg_mark')]])
    return result


def show_good_students(good_students: list):
    put_html(constants.MSG_GOOD_STUDENTS)
    put_table(
        good_students, [constants.LABEL_TABLE_NAME, constants.LABEL_TABLE_AVG_MARK]
    )


def get_avg_group_mark(students: dict) -> float:
    result = 0
    for student in students.values():
        result += student[get_form_key('avg_mark')]
    return result / len(students)


def show_avg_group_mark(avg_group_mark: float):
    put_html(constants.MSG_GROUP_AVG_MARK.format(avg_group_mark=avg_group_mark))


def get_students(students: dict) -> list:
    result = []
    for name, studentData in students.items():
        result.append([
            name, 
            studentData.get(get_form_key('avg_mark')),
            studentData.get(get_form_key('phone')) or constants.MSG_PHONE_NOT_FOUND,
            studentData.get(get_form_key('email')) or constants.MSG_EMAIL_NOT_FOUND,
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


if __name__ == '__main__':
    start_server(main, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
