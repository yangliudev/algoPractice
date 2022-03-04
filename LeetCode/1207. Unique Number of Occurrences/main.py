# a = [[1,2,3],[2,3,4],[3,4,5],[3,5,6]]
# arr = [1,2,2,1,1,3]

# set_arr = set(arr)
# list_set_arr = list(set_arr)
# print(list_set_arr)

# #arr = ''.join(map(str, list_set_arr))

# print(arr)

# nested_list = [arr, list_set_arr]
# print(nested_list)

# print(set.intersection(*map(set,nested_list)))

from typing import List

arr = [1,2,2,1,1,3]

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        my_dict = {}
        
        for i in range(len(arr)):
            key = arr[i]
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1

        result_set = set()

        for key in my_dict:
            value = my_dict[key]
            if value not in result_set:
                result_set.add(value)
            else:
                return False

        return True

print(Solution().uniqueOccurrences(arr))


# my_dict = {}

# my_dict = {1: 1}
# my_dict = {1: 2}
# my_dict = {1: 3, 2: 2, 3: 1}