from string import ascii_uppercase

def change_alpha(name):
    
    # 방향키를 어디로 해야 좀 더 효율적인지 판단하는 알고리즘. 이것보단 ord()를 써서 직접 구하는 것이 좀 더 효율적이고 코드도 짧아진다.
    # [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    up = 0
    down = 1
    # 아스키 문자에서 모든 대문자 알파벳을 뽑는다.
    alpha_list = list(ascii_uppercase)
    i = 0
    j = 0
    # A일 경우 0을 뽑아준다. 
    if name == 'A':
        return 0
        
    elif name != 'A':
        # 'A'가 아닌 경우 up 케이스와 down 케이스를 따로 구한다.
        while name != alpha_list[i]:
            for i in range(0,len(alpha_list)):
                if alpha_list[i] != name:
                    up += 1
                elif alpha_list[i] == name:
                    break
                
    
        while name != alpha_list[j]:
            for j in range(len(alpha_list)-1, -1, -1):
                if alpha_list[j] != name:
                    down += 1
                elif alpha_list[j] == name:
                    break

    # up이 더 크면 down, down이 더 크면 up, 둘 다 같으면 up을 반환한다.
    if up > down:
        return down
    
    elif up < down:
        return up
    
    elif up == down:
        return up

    
def solution(name):
    # 각 알파벳 별로 어느쪽으로 가야 효율적인지 list형태로 반환한다. 
    m = [change_alpha(c) for c in name]
    answer = 0
    where = 0
    
    # m이 모두 0이 될때까지 이 알고리즘은 돌아간다. 
    while True:
        
        # answer에 첫번째 알파벳 값을 더해준다.
        answer += m[where]
        # 더해준 값은 0으로 바꿔준다.
        m[where] = 0
        
        if sum(m) == 0:
            break

        # 위에 조건이 만족하지 못하면 left, right에 1로 지정해준다.    
        left, right = (1,1)
        
        # left 방향으로 0보다 커질 때까지 1을 더해준다
        while m[where-left] <= 0:
            left += 1
        # right 방향으로 0보다 커질 때까지 1을 더해준다.
        while m[where+right] <=0:
            right += 1
        
        # left < right 이면 answer에는 left, where애는 -left 그 외에는 right를 더해준다. 
        answer += left if left < right else right
        where += -left if left < right else right
        
    return answer