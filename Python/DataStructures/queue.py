'''

https://prismoskills.appspot.com/lessons/Algorithms/Chapter_03_-_Queue_Dequeue_and_Priority_Queue.jsp#:~:text=Queue%20is%20a%20list%20where,done%20at%20the%20other%20end.&text=Priority%20queue%20does%20not%20have,is%20in%20a%20sorted%20order.

Queue is a list where insertion is done at one end and removal is done at the other end.

Dequeue is a list where every end supports insertion and removal.
With this feature, it is possible to use the dequeue as a list and a stack at the same time as required by the application.

Priority queue does not have any ends.
In a priority queue, elements can be inserted in any order but removal of the elements is in a sorted order.
Due to this behavior, a priority queue can be used to sort the elements.

Since sorting is done only when the elements are removed from the priority queue, the PQ is easily implemented by a heap.
Using an array-based heap, elements can be inserted and deleted in O(logN).

'''