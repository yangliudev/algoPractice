# https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
# Remove all occurences of an element from a list
x = [1, 2, 3, 4, 2, 2, 3]
x[:] = (value for value in x if value != 2)
print(x)
#[1, 3, 4, 3]

# Replace all occurences of an element with another element in a list
myl = [1, 2, 3, 4, 5, 4, 4, 4, 6]
myl[:] = [x if x != 4 else 44 for x in myl]
print(myl)