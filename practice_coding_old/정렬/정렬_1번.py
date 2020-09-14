def solution(array, commands):
    answer = []
    for i in commands:
        # commands 별로 하나씩 지정. 처음부분은 지문대로 원하는 결과를 나오게 하기 위해선 -1을 해줘야함. 
        # 마지막도 마찬가지. 파이썬은 0부터 시작하기 때문. 
        a = i[0] - 1
        b = i[1]
        c = i[2] - 1 
        list1 = array[a:b]
        list1.sort()
        d = list1[c]
        # 최종 결과는 answer list 안에 넣어준다.
        answer.append(d)
    return answer
        