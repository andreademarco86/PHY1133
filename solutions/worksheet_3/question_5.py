from numpy.random import random

# Create random list from 1 to 500
mylist = (random(100) * 499 + 1).tolist()

for i in range(len(mylist)):
    # Find the next smallest element in the list
    minimum = min(mylist[i:])

    # Get the index of this element
    min_index = mylist[i:].index(minimum)

    # Replace element at min_index with first element
    mylist[i + min_index] = mylist[i]

    # replace first element with min element
    mylist[i] = minimum

# Print sorted list
print(mylist)

# Not that you can check if the list is properly sorted by
# sorting it again using python's sorted function
print(f"Is it sorted?: {mylist == sorted(mylist)}")