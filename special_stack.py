#get min number of stack using auxillary stack
class queue:
    def __init__(self):
        self.s=[]
        self.aux=[]
    def enqueue(self,x):
        self.s.append(x)
        if len(self.aux)==0:
            self.aux.append(x)
        else:
            m=self.aux[-1]
            if m>x:
                self.aux.append(x)
            else:
                self.aux.append(m)
    def getmin(self):
        min=self.aux[-1]
        return min

if __name__=='__main__':
    
    q=queue()
    q.enqueue(19)
    q.enqueue(15)
    q.enqueue(17)
    q.enqueue(29)
    q.enqueue(10)
    q.enqueue(32)
    q.enqueue(18)
    q.enqueue(16)

    print(q.getmin())

    
