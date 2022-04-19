# A visualization aid to help you better understand recursion

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# # Below is a trace of the function

# result = 6 + tri_recursion(5)
# result = 5 + tri_recursion(4)
# result = 4 + tri_recursion(3)
# result = 3 + tri_recursion(2)
# result = 2 + tri_recursion(1)
# result = 1 + tri_recursion(0)
# result = 0

# result = 6 + 15
# result = 5 + 10
# result = 4 + 6
# result = 3 + 3
# result = 2 + 1
# result = 1 + 0



# Let's practice writing some basic functions using recursion

# Factorial Function

# First look for a pattern
# 0! = 1
# 1! = 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1

def factorial(n):
  # Cover edge cases
  if n < 0:
    return False

  # Base case
  if n == 0 or n == 1:
    return 1
  
  product = n * factorial(n-1)
  return product

#print(factorial(4))

# https://stackoverflow.com/questions/5532902/python-reversing-a-string-using-recursion
def recursive_reverse(word):
  # Base case
  if word == '':
    return word
  else:
    return word[-1] + recursive_reverse(word[:-1])

#print(recursive_reverse('nbc'))

# First call - recursive_reverse('nbc')
# word[-1] + recursive_reverse(word[:-1]) == 'c' + recursive_reverse('nb')

# Second call - recursive_reverse('nb')
# word[-1] + recursive_reverse(word[:-1]) == 'b' + recursive_reverse('n')

# Third call - recursive_reverse('n')
# word[-1] + recursive_reverse(word[:-1]) == 'n' + recursive_reverse('')

# Fourth call - recursive_reverse('')
# if word == '':
#   return word

def recursive_fibonacci(n):
  # base case
  if n == 0 or n == 1:
    return n

  res = recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

  return res

# print(recursive_fibonacci(29))

# 0 1 1 2 3 5

def recursive_palindrome(word):
  if len(word) < 2:
    return True
  if word[0] != word[-1]:
    return False

  return recursive_palindrome(word[1:-1])

print(recursive_palindrome('racecar'))

def recursive_vowels(word):
  vowels = 'aeiouAEIOU'

  if word == '':
    return 0
  
  if word[0] in vowels:
    return 1 + recursive_vowels(word[1:])
  else:
    return 0 + recursive_vowels(word[1:])
  
print(recursive_vowels('aay'))

# First call - recursive_vowels('aay')
# return 1 + recursive_vowels(word[1:])
# return 1 + recursive_vowels('ay')

# Second call - recursive_vowels('ay')
# return 1 + recursive_vowels(word[1:])
# return 1 + recursive_vowels('y')

# Third call - recursive_vowels('y')
# return 0 + recursive_vowels(word[1:])
# return 0 + recursive_vowels('')

# Fourth call - recursive_vowels('') RETURNS 0

def recursive_sum(nums):
  if len(nums) == 0:
    return 0
  
  return nums[0] + recursive_sum(nums[1:])

print(recursive_sum([1,3,5,7,9]))

def recursive_reverse_list(ls):
    if len(ls) == 0:
        return []
    return [ls[-1]] + recursive_reverse_list(ls[:-1])
    
print(recursive_reverse_list([1, 2, 3]))
