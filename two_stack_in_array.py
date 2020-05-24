class twostack:
    def __init__(self,n):
        self.size=n
        self.top1=-1
        self.top2=self.size
        self.arr=[None]*n
    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1=self.top1+1
            self.arr[self.top1]=x
        else:
            print("stack is full")

    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2=self.top2-1
            self.arr[self.top2]=x
        else:
            print("stack is full")
    def pop1(self):
        x=self.arr[self.top1]
        return x
    def pop2(self):
        x=self.arr[self.top2]
        return x
if __name__=='__main__':
    t=twostack(10)
    t.push1(3)
    t.push2(4)
    t.push1(5)
    t.push1(6)
    t.push2(7)
    t.push2(8)
    t.push2(9)
    t.push2(10)

    print(t.pop1())
    print(t.pop2())
    
        
        
        
            
