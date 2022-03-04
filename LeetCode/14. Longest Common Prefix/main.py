strs = ["flower","flow","flight"]
strs2 = ["flower","dad","flight"]

if len(strs) == 0:
    print("")

min_str = min(strs)

max_str = max(strs)

for i in range(len(strs)):
    if min_str[i] != max_str[i]:
        print(min_str[:i])
print(min_str)