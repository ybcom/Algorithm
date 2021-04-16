'''
input : [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves : [1,5,3,5,1,2,1,4]
result : 4
'''
board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    result = 0
    buket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                buket.append(board[i][move-1])
                board[i][move-1] = 0
                try:
                    if buket[-1] == buket[-2]:
                        del buket[len(buket)-2 : len(buket)]
                        result+=1
                    break
                except IndexError:
                    break
    return result *2    # 뽑은 인형의 개수

if __name__ == '__main__':
    answer = solution(board, moves)

