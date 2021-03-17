def solution(p):
    if len(p) == 0:
        return p
    u, v = check_balance(p)
    if correct(u):
        return u + solution(v)
    answer = correction(u, v)
    return answer


def balance(p):
    chk = 0
    for i in p:
        if i == "(":
            chk += 1
        elif i == ")":
            chk -= 1
    if chk == 0:
        return True
    else:
        return False


def correct(p):
    stack = []
    if len(p) == 0:
        return True
    for i in p:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) != 0:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def check_balance(p):
    string = ""
    for i in p:
        string += i
        balance_chk = balance(string)
        if balance_chk:
            u = p[: len(string)]
            v = p[len(string) :]
            return u, v


def correction(u, v):
    empty = "("
    empty += solution(v)
    empty += ")"
    u = u[1:]
    u = u[:-1]
    for i in u:
        if i == "(":
            empty += ")"
        elif i == ")":
            empty += "("
    return empty