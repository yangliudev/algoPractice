# A visualization aid to help you better understand recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Below is a trace of the function

result = 6 + tri_recursion(5)
result = 5 + tri_recursion(4)
result = 4 + tri_recursion(3)
result = 3 + tri_recursion(2)
result = 2 + tri_recursion(1)
result = 1 + tri_recursion(0)
result = 0



result = 6 + 15
result = 5 + 10
result = 4 + 6
result = 3 + 3
result = 2 + 1
result = 1 + 0