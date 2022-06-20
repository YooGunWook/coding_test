def solution(number, k):
    """
    stack 기반 풀이
    순서가 유지된 상태에서 큰 수를 만들어야 하기 때문에
    끝 숫자 기준으로 다음 숫자보다 작다면 pop으로 없애준다.
    pop으로 없애게 되면 k의 개수를 사용한 것이기 때문에 k도 빼준다.
    다만 k를 전부다 쓰지 못한다면 뒤에서 k만큼 빼줘야 한다.
    """
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


if __name__ == "__main__":
    print(solution("1924", 2))
