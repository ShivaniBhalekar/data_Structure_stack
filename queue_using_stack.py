class queue:
    def __init__(self):
        
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while len(self.s1)!=0:
           self.s2.append(self.s1[-1])
           self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        x=self.s1[-1]
        self.s1.pop()
        return x

if __name__ == '__main__': 
#s1=[1,2,3,4,5,6,7]
    q=queue()
    q.enqueue(8)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(9)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
