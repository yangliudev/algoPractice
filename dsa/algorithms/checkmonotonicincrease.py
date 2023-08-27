from functools import reduce

test_list = [1, 4, 5, 7, 8, 6] 

print ("Original list : " + str(test_list)) 

res = all(i < j for i, j in zip(test_list, test_list[1:])) 

print ("Is list strictly increasing ? : " + str(res)) 


is_increasing = lambda test_list: reduce(lambda a,b: b if a < b else 9999 , test_list)!=9999
print(is_increasing)