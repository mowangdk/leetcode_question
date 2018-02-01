# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = list()
        self.min_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.normal_stack.append(x)
        if self.min_stack:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top_element = self.normal_stack.pop()
        if self.min_stack and self.min_stack[-1] == top_element:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.normal_stack:
            return self.normal_stack[-1]
        else:
            return 0

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return 0
        else:
            return self.min_stack[-1]

