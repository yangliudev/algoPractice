#Create a dictionary that holds name with index as key
# name = "yang"

# dic = {}

# for i in range(len(name)):
#     dic[i] = name[i]

# print(dic)

#Keep in mind that in a dictionary keys are UNIQUE - key value pair

#Create a dictionary that holds name with letters of name as key
# name = "yang"

# dic = {}

# for i in range(len(name)):
#     dic[name[i]] = i

# print(dic)

#Create a dictionary that holds the count of each letter in a string
# strs = 'aaaabbbccd'
# dic = {}
# for i in strs:
#     dic[i] = dic.get(i, 0) + 1

# print(dic)

# Flip keys and values in dictionary

old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23} 
  
new_dict = dict([(value, key) for key, value in old_dict.items()])
print(new_dict)

# Get key with greatest value in dictionary

dic = {'A': 67, 'B': 23, 'C': 45, 'D': 56} 

print(max(dic, key=dic.get))