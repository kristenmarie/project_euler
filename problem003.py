"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def largest_prime():
  factor = 2
  num = 600851475143
  while factor ** 2 <= num:
    if num % factor == 0:
      num /= factor
    factor += 1
  if (num > 1):
    return num
  return factor
