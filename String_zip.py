'''
같은 패턴이 나오면 앞에 숫자 붙이고 해당 패턴 중 하나 출력
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.

s = "aabbaccc"
result = 7
s = "ababcdcdababcdcd"
result = 9
'''


def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)

if __name__ == '__main__':
    s = "aabbaccc"
    solution(s)





