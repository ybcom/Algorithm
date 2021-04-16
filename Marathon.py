'''
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
return = "leo"
마라톤 참여자와 완주자가 주어지면 나머지 리턴, 동명이인이면 하나 출력
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion):
        if par != com:
            return par  # 예시 1번

    return participant[-1]

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    answer = solution(participant, completion)

