'''Write a Python program to compute the difference between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']'''

# Solution:
from collections import Counter
# creating two lists
list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

# printing the difference between two lists
calcList=Counter(list1) - Counter(list2)
final= list(calcList.elements())
print("the difference between two lists is: ",final )


