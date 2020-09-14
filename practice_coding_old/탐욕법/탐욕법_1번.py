def solution(n, lost, reserve):

    # 첫번째 조건: lost에 reserve가 있는 학생은 제외한다. 
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    # 작은 것부터 체크를 해줘야한다. 안그러면 중간에 꼬일 수 있음.
    # 최대한 전체 학생에게 주는 것이 목표임. 
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)
    
    
    return n - len(set_lost)