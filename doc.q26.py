a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print("c1","c2","c3")
# s=0
for i in a:
    # print(a[i],end=" ")
    for j in range(len(a[i])):
        # print(a[i][j])
        if j in a[i]:
            print(a[i])
        





# Sample Output:
# C1 C2 C3
# 1 5 3
# 2 6 10
# 3 7 11