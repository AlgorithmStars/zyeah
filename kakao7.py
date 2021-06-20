def move_robot(now_robot, board, N):
    next_robot = []
    for now_pos in now_robot:
        x1 = now_pos[0]
        y1 = now_pos[1]
        x2 = now_pos[2]
        y2 = now_pos[3]
        if x1 == x2:
            if x1-1 >= 0 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
                next_robot.append((x1-1,y1,x2-1,y2))
            if x2+1 < N and board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                next_robot.append((x1+1,y1,x2+1,y2))
            if y1-1 >= 0 and board[x1][y1-1] == 0:
                next_robot.append((x1,y1-1,x2,y2-1))
            if y2+1 < N and board[x2][y2+1] == 0:
                next_robot.append((x1,y1+1,x2,y2+1))
            if x1-1 >= 0 and board[x2-1][y2] == 0 and board[x1-1][y1] == 0:
                next_robot.append((x1-1,y1,x1,y1))
            if x1+1 < N and board[x2+1][y2] == 0 and board[x1+1][y1] == 0:
                next_robot.append((x1,y1,x1+1,y1))
            if x2-1 >= 0 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
                next_robot.append((x2-1,y2,x2,y2))
            if x2+1 < N and board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
                next_robot.append((x2,y2,x2+1,y2))
        else:
            if x1-1 >= 0 and board[x1-1][y1] == 0:
                next_robot.append((x1-1,y1,x2-1,y2))
            if x2+1 < N and board[x2+1][y2] == 0:
                next_robot.append((x1+1,y1,x2+1,y2))
            if y1-1 >= 0 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0:
                next_robot.append((x1,y1-1,x2,y2-1))
            if y2+1 < N and board[x1][y1+1] == 0 and board[x2][y2+1] == 0:
                next_robot.append((x1,y1+1,x2,y2+1))
            if y1-1 >= 0 and board[x2][y2-1] == 0 and board[x1][y1-1] == 0:
                next_robot.append((x1,y1-1,x1,y1))
            if y1+1 < N and board[x2][y2+1] == 0 and board[x1][y1+1] == 0:
                next_robot.append((x1,y1,x1,y1+1))
            if y2-1 >= 0 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0:
                next_robot.append((x2,y2-1,x2,y2))
            if y2+1 < N and board[x1][y1+1] == 0 and board[x2][y2+1] == 0:
                next_robot.append((x2,y2,x2,y2+1))
    return next_robot

def solution(board):
    N = len(board)
    robot = [(0, 0, 0, 1)]
    time = 0
    visited = [(0, 0, 0, 1)]
    while robot:
        next_robot = move_robot(robot, board, N)
        time += 1
        robot = []
        for r in next_robot:
            if r not in visited:
                visited.append(r)
                robot.append(r)
            if r[2] == N-1 and r[3] == N-1:
                return time
