A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]

print("list A:",A)
print("list B:",B)
mylist =  set (A) & set(B)

for i in mylist:
    print(i)

so1=list (set (A) ^ set(mylist))
print("các phần tử list a không trùng với b là:",so1)
so2=list (set (B) ^ set(mylist))
print("các phần tử list b không trùng vs a là :",so2)