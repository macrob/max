RATE = 20


class InsuranceAmountError(Exception):
  pass
if RATE.is_integer():
    print("Rate is an integer")
else:
    print("Rate is a float")

def get_insurance_amount(car_price: int | float) -> float:
  if (car_price < 0):
    # raise Exception('Car price cannot be negative')
    # raise ValueError('Car price cannot be negative')
    # raise NotImplementedError('Car price cannot be negative')
    raise InsuranceAmountError('Car price cannot be negative')
  
  summa = car_price * RATE / 100
  return summa

nissan_leaf_cost = -3000



#get_insurance_amount(nissan_leaf_cost)


def devide_two_numbers(*, devisible: float, divisor: float) -> float:
  try:
    share = devisible / divisor
  except ZeroDivisionError:
    share = 0.0
    pass
  except TypeError:
    share = 0.0
    pass

  return share

# rs = devide_two_numbers(devisible=10, divisor=0)

rs = devide_two_numbers(devisible=10, divisor='0')
print(rs)