a="cat.f,vc"
b="tfgac"

i=j=0

def check(a,b):
    if len(a)!=len(b):
        return False
    if a=="" :
        if b=="":
            return True
        else:
            return False
    i=0
    j=len(a)-1

    for _  in range(len(a)):
        if a[i]!=b[j]:
            return False
        i+=1
        j-=1
    return True

print(check(a,b))