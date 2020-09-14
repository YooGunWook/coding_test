def solution(numbers, target):
    # 시작은 0부터 하자 
    # 트리 구조를 만들어주기 위해서
    # -1 부터 시작할 수 있기 때문
    answer_list = [0]
    # numbers의 개수만큼 for문 돌린다
    for i in numbers:
        temp = []
        # j만큼 돌려서 j에 i를 돌려준다.
        for j in answer_list:
            temp.append(j+i)
            temp.append(j-i)
        # 바꿔준다
        answer_list = temp
    # target만 더해준다. 
    answer = answer_list.count(target)
    return answer