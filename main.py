# numbers = [5, -3, 8, -1, 0, 7, -9, 4]
# count_evens = 0
# count_odds = 0
# count_zeros = 0
# for number in numbers:
#     if number % 2 == 0:
#         count_evens += 1
#     elif number % 2 != 0:
#         count_odds += 1
#     else:
#         count_zeros += 1
# print(count_evens)
# print(count_odds)
# print(count_zeros)

# numbers = [1, 2, 3, 4, 5]
# squares = []
# sum = 0
# for number in numbers:
#     squares.append(number ** 2)
#     for square in squares:
#         sum += square
# print(squares)
# print(sum)

# numbers = [5, 12, 8, 25, 3, 18, 10, 30]
# list = []
# for number in numbers:
#     if number > 10:
#         list.append(number)
# print(list)

# numbers = [4, 2, 4, 7, 4, 9, 2, 4]
# target = 4
# count = 0
# for number in numbers:
#     if number == target:
#         count = count + 1
# print("The number of times 4 appears is :",count)


numbers = [1, 2, 3, 2, 4, 5, 1, 6]
list = []
seen = []
for number in numbers:
    if number in list:
        if number not in seen:
            seen.append(number)
    else:
        list.append(number)
print(list)
print(seen)

