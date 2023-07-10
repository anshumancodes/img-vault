# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.


def check(e):
    return e.count(3)>=3 and e.count(19)==2
input_list = [5, 5, 5, 19, 19, 19, 5, 5,87 ,89,47,43,11,23,4,6,90]
print(check(input_list))
