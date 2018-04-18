"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sum_square_difference():
    sqares_sum = sum(
        (i **2)
        for i in range(1,101)
        )
    numbers = range(1,101)
    total_sum_squared = sum(numbers) ** 2
    return total_sum_squared - sqares_sum