'''
greedy
 A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10

return 3
'''
A = [1,3,7,9,9]
B = [5,6,8,9,10]

sorted_val = []
for i in range(len(A)):
    sorted_val.append((A[i], B[i]))

sorted(sorted_val, key= lambda x:(x[1], x[0]))

max_num = 0
start = 0
for meet in sorted_val:
    if meet[0] > start:
        start = meet[1]
        max_num += 1
print(max_num)




