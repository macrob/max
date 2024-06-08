from pywebio.input import textarea, input as input_pw, NUMBER
from pywebio.output import put_text, put_image, put_html
from pywebio import start_server
from pywebio.session import run_js


def convert_string_to_number(input_string: str) -> int | float:
    if input_string.isdigit():
        result = int(input_string)

    is_only_on_dot_in_string = input_string.count('.') == 1
    is_only_digits_except_dots = input_string.replace('.', '').isdigit()

    if is_only_on_dot_in_string and is_only_digits_except_dots:
        result = float(input_string)

    return result


def get_triangle_area(catet1: int | float, catet2: int | float) -> int | float:
    result = catet1 * catet2 / 2
    return result


def get_formatted_html_h2(message: str) -> str:
    result_h2 = f'<h2>{message}</h2>'
    return result_h2


def main():
    catet1 = input_pw('Введіть 1 катет трикутника')
    catet2 = input_pw('Введіть 2 катет трикутника', type=NUMBER)
    catet1 = convert_string_to_number(catet1)
    triangle_area = get_triangle_area(catet1, catet2)
    put_text(f'Площа трикутника: {triangle_area}')

    run_js('setTimeout(function() { location.reload(); }, 5000);')
    return


if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
