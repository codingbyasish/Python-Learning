
number = [1, 2, 3, 4, 5, 6]

def even(num):
    return num % 2 == 0


even_lamba = lambda num: num % 2 == 0

even_numbers = filter(even, number)
print(list(even_numbers))
