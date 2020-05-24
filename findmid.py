class stack:
    def __init__(self):
        self.s=[1,2,3,4,5,6,7]
        self.ptr1=0
        self.ptr2=0
    def findmid(self):
        n=len(self.s)
        for i in range(0,n):
            while (self.ptr1!=n-1 and self.ptr2!=n-1):
                self.ptr1=self.ptr1+1
                self.ptr2=self.ptr2+2
                x=self.s[self.ptr1]
        return x

st=stack()
print(st.findmid())

        
            
        
            
            
        
