from Stack import Stack
def dec_bin(Stack,num):
  while(num!=0):
    Stack.push(num%2)
    num //= 2
    # num = int(num)
  bin = ""
  while not Stack.is_empty():
    bin += str(Stack.pop())
  return bin

stack = Stack() 
print(dec_bin(Stack=stack,num=15))