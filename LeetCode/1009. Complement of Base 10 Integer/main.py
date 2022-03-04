from typing import List

N = 5

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)[2:]
        list_binary = list(binary)

        for i in range(len(list_binary)):
            if list_binary[i] == '0':
                list_binary[i] = '1'
            elif list_binary[i] == '1':
                list_binary[i] = '0'

        strs = ''.join(list_binary)
        return int(strs, 2)
        

print(Solution().bitwiseComplement(N))