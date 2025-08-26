import math

def filter_squares(num_list):
    result = [num for num in num_list if num >=0 and math.isqrt(num) ** 2 == num]
    return result

# Test
numbers = [4, 7, 9, 12, 16, 18, 25, 26, 30]
print(filter_squares(numbers))  # ➞ [4, 9, 16, 25]
