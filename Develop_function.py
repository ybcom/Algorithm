'''
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
progresses = [93, 30, 55]
speeds = [1,30,5]
return = [2,1]
'''

# calc = progresses.copy()
# result = []


def solution(progresses, speeds):
    calc = progresses.copy()
    result = []

    while calc:
        count = 0
        calc = [i + j for i, j in zip(calc, speeds)]
        for i in range(len(calc)):
            if calc[0] >= 100:
                calc.pop(0)
                count += 1
            else:
                break
        if count != 0:
            result.append(count)

    return result

if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1,30,5]
    # progresses = [95, 90, 99, 99, 80, 99]
    # speeds = [1, 1, 1, 1, 1, 1]
    solution(progresses, speeds)


