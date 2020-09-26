'''
stack을 기반으로 진행
value가 stack의 마지막 값보다 큰 경우에 k를 1씩 제거하고 stack.pop()을 해준다
value를 계속 추가해준다.
최종적으로 k를 채우지 못했을 경우 마지막 값만 제거해준다. - > 충분히 제거되었기 때
'''


def solution(number, k):
    stack = [number[0]]
    for value in number[1:]:
        while len(stack) > 0 and stack[-1] < value and k > 0:
            k -= 1
            stack.pop()
        stack.append(value)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
