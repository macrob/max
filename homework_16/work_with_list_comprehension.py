import sys

numbers_list = [2, 7, 11, 15, 90] * 1000000

target_list = []

for number in numbers_list:
    target_list.append(number * 2)

# print(target_list)


target_list_2 = [number * 2
                 for number in numbers_list
                 if number > 10]


# target_list_3 = {number: number * 2 for number in numbers_list if number > 10} # set
# target_list_4 = {number: number * 2 for number in numbers_list if number > 10} # dictionary
# target_list_5 = [{number: number * 2} for number in numbers_list if number > 10] # list[dictionary]

target_list_6 = (number * 2 for number in numbers_list if number > 10) # generator

for i in target_list_6:
  print(i)
print(sys.getsizeof(target_list))
print(sys.getsizeof(target_list_6))
