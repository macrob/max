from pywebio import start_server
from pywebio.input import textarea, input as input_pw, NUMBER, DATE, TEXT
from pywebio.output import put_text, put_image, put_html
from pywebio.session import run_js

import config
import constants


def print_h1_header(message: str) -> str:
    header = f'<h1>{message}</h1>'
    return header


def request_username() -> str:
    return input_pw(constants.USERNAME_REQUEST).strip()


def print_question(question: str, answer: str, question_type: str) -> bool:

    user_answer = input_pw(question, type=question_type)

    if question_type == TEXT:
        user_answer = user_answer.lower()
        answer = answer.lower()

    if user_answer == answer:
        return True
    else:
        return False


def print_final_score(username: str, score: int) -> None:
    put_html(constants.MSG_FINAL_SCORE.format(username=username, score=score))


def print_page_reloader():
    timeout = str(config.PAGE_RELOAD_INTERVAL * 1000)
    reload_js = 'setTimeout(function() { location.reload(); }, ' + timeout +');'
    run_js(reload_js)


def main():
    print_h1_header(constants.PAGE_HEADER)

    total_score = 0

    username = request_username()
    answer = print_question(
        constants.QUESTION_1, constants.QUESTION_1_ANSWER, constants.QUESTION_1_TYPE
    )
    if answer:
        total_score += 1

    answer = print_question(
        constants.QUESTION_2, constants.QUESTION_2_ANSWER, constants.QUESTION_2_TYPE
    )
    if answer:
        total_score += 1

    answer = print_question(
        constants.QUESTION_3, constants.QUESTION_3_ANSWER, constants.QUESTION_3_TYPE
    )
    if answer:
        total_score += 1

    answer = print_question(
        constants.QUESTION_4, constants.QUESTION_4_ANSWER, constants.QUESTION_4_TYPE
    )
    if answer:
        total_score += 1

    answer = print_question(
        constants.QUESTION_5, constants.QUESTION_5_ANSWER, constants.QUESTION_5_TYPE
    )
    if answer:
        total_score += 1

    print_final_score(username, total_score)
    print_page_reloader()
    return


if __name__ == '__main__':
    start_server(main, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
