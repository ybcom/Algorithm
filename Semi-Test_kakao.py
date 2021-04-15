'''
Test case : [1,3,2,4,2], [1,2,3,4,5]
return : [1,2,3], [1]
'''
answer = [1,3,2,4,2]
answer_len = len(answer)

a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

a_len = len(a)
b_len = len(b)
c_len = len(c)

if answer_len / a_len > 1:
    a *= ((answer_len // a_len)+1)
if answer_len / b_len > 1:
    b *= ((answer_len // b_len)+1)
if answer_len / c_len > 1:
    c *= ((answer_len // c_len)+1)

a_arr = [1] * answer_len
b_arr = [2] * answer_len
c_arr = [3] * answer_len
# 같지 않으면 pop
for i in range(answer_len):
    if answer[i] != a[i]:
        a_arr.pop()
    if answer[i] != b[i]:
        b_arr.pop()
    if answer[i] != c[i]:
        c_arr.pop()
len_list = [len(a_arr), len(b_arr), len(c_arr)]
max_val = max(len_list)

result = []
for i, val in enumerate(len_list):
    if val == max_val:
        result.append(i+1)
print(result)