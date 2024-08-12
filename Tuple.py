# Write a function that takes a tuple of numbers and returns the smallest number in the tuple.

def find_smallest_number(numbers):
    smallest = min(numbers)
    print("The smallest number is:", smallest)

my_tuple = (99, 49, 100, 50, 70, 55)
find_smallest_number(my_tuple)

