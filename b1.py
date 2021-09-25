so1 = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
print("so1: ", so1)
print("so2: ")
for i in range(0, 15):
    if(so1[i] < 30):
        so2 = so1[i]
        print(so2, end=", ")
print("Nhập a: ")
a = input("")
print("Những số nhỏ hơn a là: ")
for i in range(0, 15):
    if(so1[i] < int(a)):
        so3 = so1[i]
        print(so3, end=", ")