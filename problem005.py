"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def smallest_multiple():
  # Number has to be at least be 2520, since answer for 1-10 is 2520.
  i = 2520
  ## Only check 11-20 since 1-10 are all factors of these numbers
  while i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0:
    i += 2520
  return i

## OR

def smallest_check(num):
  for i in range(1,21):
    if num % i == 0:
      continue
    else:
      return False
  return True

def get_smallest():
  num = 2520
  while not smallest_check(num):
    num += 2520
  return num;




