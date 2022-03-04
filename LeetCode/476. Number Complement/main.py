num = 5

class Solution:
    def findComplement(self, num: int) -> int:

        binary = bin(num)[2:]
        list_binary = list(binary)

        for i in range(len(list_binary)):
            if list_binary[i] == '0':
                list_binary[i] = '1'
            elif list_binary[i] == '1':
                list_binary[i] = '0'

        binary = ''.join(list_binary)
        return int(binary,2)
        
print(Solution().findComplement(num))