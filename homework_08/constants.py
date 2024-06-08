from pywebio.input import input, textarea, input as input_pw, NUMBER, DATE, TEXT
PAGE_HEADER = 'Вікторина "любов до пайтона"'

USERNAME_REQUEST = "Введіть ваше ім'я"

QUESTION_1 = 'В якому року була випущена перша версія Python?'  # ANSWER: 1991
QUESTION_1_ANSWER = 1991
QUESTION_1_TYPE = NUMBER

QUESTION_2 = 'Як отримати правила сформульовані в "The Zen of Python"' # ANSWER: import this
QUESTION_2_ANSWER = 'import this'
QUESTION_2_TYPE = TEXT

QUESTION_3 = 'Як називається тип данних для цілих чисел?'  # ANSWER: int
QUESTION_3_ANSWER = 'int'
QUESTION_3_TYPE = TEXT

QUESTION_4 = 'Яка з цих операцій (+, -, *, /) може бути використана для роботи з рядками в Python?'  # ANSWER: +
QUESTION_4_ANSWER = '+'
QUESTION_4_TYPE = TEXT

QUESTION_5 = 'Скільки різних арифметичних операцій можна виконати над двома числами в Python?'  # ANSWER: 7
QUESTION_5_ANSWER = 7
QUESTION_5_TYPE = NUMBER

MSG_WRONG_ANSWER = 'Невірно!'
MSG_CORRECT_ANSWER = 'Вірно!'

MSG_FINAL_SCORE = '<h1>{username}</h1>Ваша оцінка становить: <b>{score} балів</b>'