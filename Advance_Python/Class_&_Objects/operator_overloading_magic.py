class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def __gt__(self,other):
        return self.mark>=self.other
    def __ls__(self,other):
        return self.mark<=self.other

s1=student('siddharth',67)
s2=student('venketesh',78)
print('s1>s2',s1>s2)
print('s1<s2',s1<s2)
print('s1>=s2',s1>=s2)
print('s1<=s2',s1<=s2)
    
