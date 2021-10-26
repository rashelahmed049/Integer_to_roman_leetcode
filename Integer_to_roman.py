def roman(n):
    d = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],
    ["CD",400],["D",500],["CM",900],["M",1000]]
    res=""
    for sys,v in reversed(d):
        if n//v:
            c = n//v
            res+=sys*c
            n = n%v
        if n==0:
            break
    return res

n = 6
print(roman(6))
