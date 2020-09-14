import itertools

def count_all(numbers):
    num_list = [] # 전체 순열 넣어줄 리스트
    for i in range(1,len(numbers)+1) : # 한자리 숫자부터 numbers 길이 만큼의 숫자로 순열을 만든다.
        test_list = itertools.permutations(numbers,i)
        for j in test_list : # test_list안에 있는 값들을 int로 바꿔주고 num_list에 넣어준다. 
            num_list.append(int("".join(j)))
            print(j)
        
    num_list = list(set(num_list)) # 중복 제외
    return num_list
        
def is_prime(number):
    if number <= 1: # 1과 1보다 작은 경우는 소수가 아니므로 False
        return False
    elif number == 2: # 2는 짝수 중 유일한 소수다.
        return True
    else:
        for i in range(2, number): # number-1 때까지 for문을 돌렸을 때 나머지가 0이 아니면 True다.
            if (number % i) == 0:
                break
            elif i == number -1 :
                return True
    
def solution(numbers):
    count_perm = count_all(numbers)
    answer = 0
    # count_perm 안에 있는 값들을 조회한다. 
    for i in range(0,len(count_perm)):
        if is_prime(count_perm[i]) == True:
            answer += 1
            print(count_perm[i])
        else:
            pass
    return answer
