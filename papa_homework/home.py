list_of_random_numbers = [9, 22, 11, 33, 50, 311, 155, 63, 324]

# need to find max value
# need to find min value

# count of elements
# need to find sum of all elements
# need to find average of all elements

# need to find all elements that are greater than 10
# need to find all even elements
# need to find all odd elements
# need to find all elements which are divisible by 3 without a remainder
# count the number of elements where the remainder of division is equal to 2

# need to sort the array in descending order
res = []
max = list_of_random_numbers[0]

i = range(len(list_of_random_numbers))
print(i)
for iterator in range(len(list_of_random_numbers)):
  for i in range(len(list_of_random_numbers)-1):
    a = list_of_random_numbers[i]
    b = list_of_random_numbers[i+1]
    print (a, b)
    if a < b:
      print (b,'--->' ,a)
      list_of_random_numbers[i] = b
      list_of_random_numbers[i+1] = a



print(list_of_random_numbers);

list_of_random_strings = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "iceberg",
]


list1 = [
    "apple",
    "banana",
    "cherry",
]

list2 = [
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "iceberg",
]

list3 = [
  ['apple', 'date'],
  ['banana', 'elderberry'],
  ['cherry', 'fig'],
  ['', 'grape'],
  ['', 'honeydew'],
  ['', 'iceberg'], 
]
# need to find the first element in the list
# need to find the last element in the list
# need to find the longest element in the list
# need to find the shorter element in the lst
# need to find average length of all elements
# need to count the number of elements in the list
# need to count the number of elements in the list that are longer than 5 characters
# need to count the number of elements in the list that are shorter than 5 characters
# need to count the number of elements in the list that are longer than 5 characters and shorter than 10 characters
# need to count the number of elements that have first charter as "a"



while range(5):
  print('tetet')