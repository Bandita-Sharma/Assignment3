#Que1-->Create a list with user defined inputs
l1=['hi','Bandita','here']
print(l1)
print()

#Que2-->Add the following list to above created list: ['google','apple','facebook','microsoft','tesla']
l2=['google','apple','facebook','microsoft','tesla']
l1.extend(l2)
print(l1)
print()

#Que3-->Count the number of time an object occurs in a list
l1=['hello','i','am','abc','and','i','am','xyz']
print(l1)
a=l1.count('i')
print("count of i in the above list:",end='')
print(a)
print()

#Que4-->Create a list with numbers and sort it in ascending order
l2=[3,1,7,9,10,47,24,2]
l2.sort()
print(l2)
print()

#Que5-->Given are two one-dimensional arrays A and B which are sorted in ascending order .Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order.
l3=[2,5,8,10]
l4=[1,7,12,15,16]
l5=l3+l4
l5.sort()
print(l5)
print()

#Que6-->Implement a stack and queue using lists.
"""stack is a data structure which follows a particular order that could be last in first out or first in last out"""
stack=['abc','def']
stack.append('ghi')
stack.append('jkl')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

"""queue is a data structure in which insertion and deletion happens at different ends"""
queue=['abc','def','gih']
queue.append('jkl')
queue.append('mno')
print(queue)
queue.remove('abc')
print(queue)
queue.remove('def')
print(queue)
print()

#Que7-->Count even and odd numbers in that list.
list=[2,5,7,9,10,34,56,79,13,57,77]
even_count=0
for i in range(len(list)):
    if list[i] % 2 == 0:
        even_count=even_count+1
print("count of even numbers is :" ,even_count)

odd_count=0
for i in range(len(list)):
    if list[i] % 2 != 0:
        odd_count=odd_count+1
print("count of odd numbers is :" ,odd_count)
