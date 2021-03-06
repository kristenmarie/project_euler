"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def even_sum():
    total = 0
    current_num = 1
    next_num = 2
    while current_num <= 4000000:
        if current_num % 2 == 0:
        total += current_num
    new_next = current_num + next_num
    current_num = next_num
    next_num = new_next
    return total
