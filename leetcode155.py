class MinStack:
    def __int__(self):
        self.stk = []
        self.min_stk = []
    
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk)[-1]
        else:
            self.min_stk.append(val)
    
    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
    
    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.stk_min[-1]
    
#time: O(1)   space: O(n)