def check_pilar(frame, x, y):
    if frame[x][y][0] == 1:
        if y == 0:
            return True
        if frame[x][y-1][0] == 1:
            return True
        if frame[x-1][y][1] or frame[x][y][1]:
            return True
        return False
    else:
        return True

def check_crossbeam(frame, x, y):
    if frame[x][y][1] == 1:
        if (frame[x][y-1][0] + frame[x+1][y-1][0]) > 0:
            return True
        if (frame[x-1][y][1] * frame[x+1][y][1]) == 1:
            return True
        return False
    else:
        return True

def change_frame(n, frame, x, y, a, b):
    frame[x][y][a] = b
    for i in range(n+1):
        for j in range(n+1):
            if not check_pilar(frame, i, j):
                frame[x][y][a] = (b+1)%2
                return frame[x][y][a]
            if not check_crossbeam(frame, i, j):
                frame[x][y][a] = (b+1)%2
                return frame[x][y][a]
    return frame[x][y][a]

def solution(n, build_frame):
    frame = [[[0,0] for i in range(n+1)] for j in range(n+1)]
    for pole in build_frame:
        x, y, a, b = pole
        frame[x][y][a] = change_frame(n, frame, x, y, a, b)

    answer = []
    for x in range(n+1):
        for y in range(n+1):
            for a in range(2):
                if frame[x][y][a] == 1:
                    answer.append([x, y, a])
    return answer
