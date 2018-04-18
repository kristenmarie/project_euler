# Find the largest palindrome made from the product of two 3 digit numbers

# def largest_palindrome():
#   largest = 0
#   for first in range(100, 1000):
#     for second in range(100, 1000):
#       if str(first * second) == str(first * second)[::-1] and first * second > largest:
#         largest = first * second
#   return largest

def largest_palindrome():
  largest = max(
    (first * second) 
    for first in range(100, 1000) 
    for second in range(100,1000) 
    if str(first * second) == str(first * second)[::-1]
  )

  return largest
  