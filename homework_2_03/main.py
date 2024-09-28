### 
# Створити функцію, яка приймає два списки і повертає True, якщо в першому списку парних елементів більше, ніж НЕПАРНИХ у другому.
# Наприклад: для списків [1, 10, 4, 13, 22, 10, 0 , 100, 12, 14, 105] та [1, 1, 3, 13, 22, 5 , 17] повинно повернути True.


list_1 = [1, 10, 4, 13, 22, 10, 0 , 100, 12, 14, 105]
list_2 = [1, 1, 3, 13, 22, 5 , 17]

def compare_lists(list_1, list_2):
    even_count = 0
    odd_count = 0

    # calculate even count in list_1
    for i in list_1:
        if i % 2 == 0:
            even_count += 1

    # calculate odd count in list_2
    for i in list_2:
        if i % 2 != 0:
            odd_count += 1

    return even_count > odd_count

print(compare_lists(list_1, list_2)) ## True


#### Створити функцію, яка приймає один список та повертає найбільший парний елемент. 
# Наприклад: [1, 10, 4, 13, 22, 10, 0 , 105, 12, 11, 105] для цього списку повинно повернути 22

def max_even_element(list_1):
    list_1.sort(reverse=True)

    for i in list_1:
        if i % 2 == 0:
            return i

max_evn = max_even_element([1, 10, 4, 13, 22, 10, 0 , 105, 12, 124, 11, 105]);
print(max_evn) ## 124

### Створити функцію, яка приймає один список та повертає три максимуми зі списку. (
# Наприклад список [1, 10, 4, 13, 22, 10, 0 , 105, 12, 11, 105]. max_1 = 105, max_2 = 22. max_3 == 13 )

def max_3_elements(list_1):
    list_1.sort(reverse=True)
    return list_1[:3]

max_3 = max_3_elements([1, 10, 4, 13, 22, 10, 0 , 105, 12, 11, 105])
print(max_3) ## [105, 22, 13]
