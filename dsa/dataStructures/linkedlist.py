# Create a linkedlist (binary search interleaved)

res_head = LLNode(interleaved[0])
tail = res_head

i = 1
while i < len(interleaved):
    tail.next = LLNode(interleaved[i])
    tail = tail.next
    i += 1

return res_head