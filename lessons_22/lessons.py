def add_two_numbers(a: int | float, b: int | float) -> float:
    if a == 55:
        raise ValueError("a is 55")
    
    return float(a + b)

def add_two_numbers_bla(a: int | float, b: int | float) -> float:
    """ according to task DEV-1 bla bla bla """
    if a == 0:
        return 0.0

    return add_two_numbers(a, b)


def multiply_by(number: int, by: int = 2) -> int:
    return number * by

def get_two_time_string(number: int) -> str:
    return str(multiply_by(number))

