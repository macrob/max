

def get_discount_price(price: float, discount: float) -> float:
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number")
    if not isinstance(discount, (int, float)):
        raise ValueError("Discount must be a number")
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    if discount < 0:
        raise ValueError("Discount must be greater or equal to 0")
    if discount > 99:
        raise ValueError("Discount must be less than 100")

    return price - price * discount / 100