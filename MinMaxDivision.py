'''
K = 3, M = 5일 때, 최소 합
A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
'''
A = [2,1,5,1,2,2,2]
K=3
if len(A) < 1:
    print(1)

sorted(A)

A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10

A = [1,3,7,9,9]
B = [10,6,8,9,5]
meeting = []
for i in range(len(A)):
    meeting.append((A[i], B[i]))

sorted(meeting, key = lambda x: (x[1], x[0]))


