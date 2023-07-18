'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

EXAMPLE

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

INITIAL CODE:

class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''

class MinStack:

    def __init__(self):
        self.stackContents=[]
        self.stackMin=[]


    def push(self, val: int) -> None:
        self.stackContents.append(val)
        if self.stackMin==[]:
            self.stackMin.append(val)
        else:
            if self.stackMin[len(self.stackMin)-1]>val:
                self.stackMin.append(val)
            else:
                self.stackMin.append(self.stackMin[len(self.stackMin)-1])

    def pop(self) -> None:
        self.stackContents.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stackContents[len(self.stackContents)-1]

    def getMin(self) -> int:
        return self.stackMin[len(self.stackMin)-1]
    
obj = MinStack()
obj.push(5)
print(obj.stackContents)
obj.push(6)
print(obj.stackContents)
obj.pop()
print(obj.stackContents)
obj.push(16)
print(obj.stackContents)
param_3 = obj.top()
print(param_3)
obj.push(3)
print(obj.stackContents)
param_4 = obj.getMin()
print(param_4)