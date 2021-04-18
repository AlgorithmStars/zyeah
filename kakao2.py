def divide_uv(p):
    num1 = 0
    num2 = 0
    for pp in p:
        if pp == p[0]:
            num1 += 1
        else:
            num2 += 1
            if num1 == num2:
                u = p[:2*num1]
                v = p[2*num1:]
                return u, v

def make_valid(u, v):
    if u[0] == '(':
        answer = u+v
    else:
        answer = ['(']+v+[')']
        answer = answer + [')' if uu == '(' else '(' for uu in u[1:-1]]
    return answer


def recursive(p):
    p = list(p)
    u, v = divide_uv(p)
    if v != []:
        v = recursive(v)
    return make_valid(u, v)

def solution(p):
    return ''.join(recursive(p))
