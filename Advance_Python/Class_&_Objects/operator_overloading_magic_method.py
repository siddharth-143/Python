class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def __gt__(self,other):
        return self.mark>=other.mark
    def __ls__(self,other):
        return self.mark<=other.mark

s1=student('siddharth',67)
s2=student('venketesh',78)
print('s1>s2 :',s1>s2)
print('s1<s2 :',s1<s2)
print('s1==s2 : ',s1==s2)
# print('s1>=s2 : ',s1>=s2)
TypeError: '>=' not supported between instances of 'student' and 'student'print('s1<=s2 :',s1<=s2)

#print('s1<=s2 : ',s1<=s2)
#TypeError: '<=' not supported between instances of 'student' and 'student'
    
