'''
전체 n명 중, lost 인원에게 체육복을 빌려줘서 총 몇명이 체육할 수 있는가
n = 5
lost = [2, 4]
reserve = [1, 3, 5]
return = 5
'''
n = 5
lost = [2, 4]
reserve = [1, 3, 5]
reserve = [3]
result = []

Total_students = list(range(1,n+1))
del Total_students[lost in Total_students]



Total_students.remove(lost)


result.extend(reserve)

for i in range(len(reserve)):
    minus_re = reserve[i]-1
    plus_re = reserve[i]+1
    if minus_re in lost:
        result.append(minus_re)
        lost.pop(lost.index(minus_re))
    elif plus_re in lost:
        result.append(plus_re)
        lost.pop(lost.index(plus_re))
    else:
        continue
print(len(result))
