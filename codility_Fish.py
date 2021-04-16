'''
A[P] > A[Q] P가 Q를 잡아먹음
살아남은 물고기 수 리턴
1,0 순서 관계만 체크
  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
'''
A = [4,3,2,1,5]
B = [0,1,0,0,0]

if len(A) == 1:
    print(1)

arr = []

for i in range(len(A)):
    arr.append((A[i], B[i]))

arr_ = []
arr_.append(arr[0])

for i in range(1, len(arr)):
    # 충돌하면
    while (True):
        if arr[i][1] == 0 and arr_[len(arr_) - 1][1] == 1:
            # 기존 물고기가 더 쎄면
            if arr[i][0] < arr_[len(arr_) - 1][0]:
                break
            # 새로운 물고기가 더 쎄면
            else:
                del arr_[len(arr_) - 1]
                if len(arr_) == 0:
                    arr_.append(arr[i])
                    break
        else:
            arr_.append(arr[i])
            break


print(len(arr_))

