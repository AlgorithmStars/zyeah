import numpy as np

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = np.array([[0 for i in range(n)] for j in range(m)])
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def solution(key, lock):
    lock = np.array(lock)
    key = np.array(key)

    N = len(lock)
    M = len(key)

    new_lock = np.array([[0 for i in range(N+2*M)] for j in range(N+2*M)])
    new_lock[M:M+N, M:M+N] = new_lock[M:M+N, M:M+N] + lock

    for k in range(4):
        for i in range(1, N+M):
            for j in range(1, N+M):
                new_lock[i:i+M, j:j+M] = new_lock[i:i+M, j:j+M] + key
                if np.all(new_lock[M:M+N, M:M+N] == 1):
                    return True
                new_lock[i:i+M, j:j+M] = new_lock[i:i+M, j:j+M] - key
        key = rotate_a_matrix_by_90_degree(key)

    return False
