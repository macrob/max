from discount import get_discount_price
import pytest

class TestGetDiscountPrice():
    def test_get_discount_price(self):
        price = 100
        discount = 10
        expected = 90
        actual = get_discount_price(price, discount)
        assert actual == expected, f"Expected {expected}, but got {actual}"

    def test_get_discount_price_negative(self):
        price = -100
        discount = 10
        with pytest.raises(ValueError):
            get_discount_price(price, discount)

    def test_get_discount_price_discount_negative(self):
        price = 100
        discount = -10
        with pytest.raises(ValueError):
            get_discount_price(price, discount)
    
    def test_get_discount_price_discount_more_than_100(self):
        price = 100
        discount = 101
        with pytest.raises(ValueError):
            get_discount_price(price, discount)

    def test_get_discount_price_price_not_number(self):
        price = "100"
        discount = 10
        with pytest.raises(ValueError):
            get_discount_price(price, discount)

    def test_get_discount_price_discount_not_number(self):
        price = 100
        discount = "10"
        with pytest.raises(ValueError):
            get_discount_price(price, discount)

    def test_get_discount_price_price_zero(self):
        price = 0
        discount = 10
        with pytest.raises(ValueError):
            get_discount_price(price, discount)