import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# assigning bstree BinarySearchTree Data structure passing in list_names[0]
bstree = BinarySearchTree(names_1[0])
#range from 1 - 10000
for i in range(1, len(names_1)):
    #running bstree on names_1 txt file
    bstree.insert(names_1[i])

duplicates = []
#loop through names_2 txt file
for name in names_2:
    #if bstree from names_1 contains the name in names_2
    if bstree.contains(name):
        #append the duplicate name to the duplicates array
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

