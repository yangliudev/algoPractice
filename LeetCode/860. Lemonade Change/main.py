'''
[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
nine 5s

[5,5,20,5,5,10,5,10,5,20]

my_dict = {
            '5': 2,
            '10': 0,
            '20': 0
        }

if i receive a 20 but there are no 10s and no 5s RETURN F
if i receive a 20 but there are no 5s RETURN F

three 5s or one 10 and one 5
'''

from typing import List

bills = [5,5,20,5,5,10,5,10,5,20]

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # my_dict = {}
        # cost = 5

        # if bills[0] != 5:
        #     return False

        # for i in range(len(bills)):
        #     my_dict[i] = bills[i]

        # for i in my_dict:


        # return my_dict

        my_dict = {
            '5': 0,
            '10': 0,
            '20': 0
        }

        for i in range(len(bills)):
            if bills[0] != 5:
                return False

            if bills[i] == 5:
                my_dict['5'] += 1

            if bills[i] == 10 and my_dict['5'] == 0:
                return False
            elif bills[i] == 10 and my_dict['5'] != 0:
                my_dict['10'] += 1
                my_dict['5'] -= 1

            if bills[i] == 20 and my_dict['10'] == 0 and my_dict['5'] == 0:
                return False
            elif bills[i] == 20 and my_dict['10'] == 0 and my_dict['5'] < 3:
                return False
            elif bills[i] == 20 and my_dict['5'] == 0:
                return False
            elif bills[i] == 20 and my_dict['10'] != 0 and my_dict['5'] != 0:
                my_dict['20'] += 1
                my_dict['10'] -= 1
                my_dict['5'] -= 1
                continue
            elif bills[i] == 20 and my_dict['5'] > 2:
                my_dict['20'] += 1
                my_dict['5'] -= 3

        return True
        
print(Solution().lemonadeChange(bills))