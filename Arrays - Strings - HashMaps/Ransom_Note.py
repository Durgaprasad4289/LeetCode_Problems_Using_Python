class Solution(object):
    def canConstruct(self, r, m):

        if len(r)>len(m):
            return False
        c1={}
        c2={}
        for i in r:
            if i in c1:
                c1[i]+=1
            else:
                c1[i]=1
        for i in m:
            if i in c2:
                c2[i]+=1
            else:
                c2[i]=1
        
        for i in r:
            if i not in c2:
                return False
            if c1[i]>c2[i]:
                return False
        return True
    
    

        