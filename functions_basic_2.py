"""
1 -Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]
"""
# def countdown_func(num):
#     result = []
#     for i in range(num, -1, -1):
#         result.append(i)
#     return result
# list_countdown = countdown_func(8)
# print(list_countdown)

"""
2 - First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
"""
def first_plus_length(list):
    sum = 0
    if not list:
        return "list is empty"
    else:
        sum = list[0] + len(list)
        print(sum)
    return sum
first_plus_length([1,2,3,4,5])
