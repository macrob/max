## 
# 
# 
# Створити функцію, яка приймає два списки і повертає True, якщо в першому списку парних елементів більше, ніж НЕПАРНИХ у другому.
# Наприклад: для списків [1, 10, 4, 13, 22, 10, 0 , 100, 12, 14, 105] та [1, 1, 3, 13, 22, 5 , 17] повинно повернути True.


list_1 = [1, 10, 4, 13, 22, 10, 0 , 100, 12, 14, 105]
list_2 = [1, 1, 3, 13, 22, 5 , 17]

def compare_lists(list_1, list_2):
    even_count = 0
    odd_count = 0

    for i in list_1:
        if i % 2 == 0:
            even_count += 1

    for i in list_2:
        if i % 2 != 0:
            odd_count += 1

    return even_count > odd_count

print(compare_lists(list_1, list_2))