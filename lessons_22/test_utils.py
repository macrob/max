from lessons import add_two_numbers, get_two_time_string
import pytest
import random

# def test_add_two_numbers():
#     a = 2
#     b = 3
#     excepted = 5.0
#     actual_result = add_two_numbers(a, b)
#     assert actual_result == excepted, f"Expected {excepted}, but got {actual_result}"
#     # pass
#     # 1/0

# def test_add_two_numbers_zero():
#     a = 0
#     b = 0
#     expected = 0.0
#     actual_result = add_two_numbers(a, b)
#     assert actual_result == expected, f"Expected {expected}, but got {actual_result}"

# def test_add_two_numbers_negative():
#     a = -2
#     b = -3
#     expected = -5.0
#     actual_result = add_two_numbers(a, b)
#     assert actual_result == expected, f"Expected {expected}, but got {actual_result}"




class TestAddTwoNumbers:
    testing_data = [(2,3,5.0), (0,0,0.0), (-2,-3,-5.0)]

    @pytest.mark.parametrize('a, b, exptected_result', testing_data)
    def test_add_two_numbers_combined(self, a, b, exptected_result):
        actual_result = add_two_numbers(a, b)
        assert actual_result == exptected_result, f"Expected {exptected_result}, but got {actual_result}"


    testing_data_fail = [
        (55, 3, 58.0)
    ]

    @pytest.mark.skip(reason="Not implemented yet")
    @pytest.mark.parametrize('a, b, exptected_result', testing_data_fail)
    def test_add_two_numbers_combined_skipped(self, a, b, exptected_result):
        actual_result = add_two_numbers(a, b)
        assert actual_result == exptected_result, f"Expected {exptected_result}, but got {actual_result}"


    def test_add_two_numbers_random(self):
        a = random.randint(0, 10**10)
        b = random.randint(0, 10**10)
        actual_result = add_two_numbers(a, b)
        assert actual_result == float(a + b), f"Expected {float(a + b)}, but got {actual_result}"
        # assert False, f"This test is failed {a} and {b}"


    @pytest.mark.parametrize('a, b, exptected_result', testing_data_fail)
    def test_add_two_numbers_combined_raise_error(self, a, b, exptected_result):
        with pytest.raises(ValueError):
            add_two_numbers(a, b)


def test_new_func():
    given = 6
    excepted = '12'
    actual_result = get_two_time_string(number=given)

    assert actual_result == excepted, f"Expected {excepted}, but got {actual_result}"
