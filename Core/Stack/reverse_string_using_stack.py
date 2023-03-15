# input_str = "Educative"
# print(input_str[::-1])

# using Stack
"""
Stack Data Structure.
"""
from Stack import Stack
    

def reverse_string(Stack,input_str):
    for i in range(len(input_str)):
      Stack.push(input_str[i])
    rev_str = ""
    while not Stack.is_empty():
      rev_str += Stack.pop()
    #   print(Stack.pop())
    return rev_str


stack = Stack()
input_str = "Shivam is the best"
print(reverse_string(Stack=stack,input_str=input_str))